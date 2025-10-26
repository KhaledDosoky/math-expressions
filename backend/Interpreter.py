import json
import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
# IMPORTANT: These imports must point to your generated ANTLR files
# Assuming ExprParser, ExprVisitor, and ExprLexer are in the current directory
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor
from ExprLexer import ExprLexer


# Helper function to format the error output
def format_error(error_info, error_type="Runtime Error"):
    """Formats the error message to include source code context."""
    line_num = error_info['line']
    col_num = error_info['column']
    source_line = error_info['source_line'].rstrip()
    
    # 1. Define the fixed-width prefix for the line number bar.
    #    "Line 5    | " is 10 characters wide (Line + 1 space + 4 digits + 4 spaces + | + 1 space).
    #    Let's calculate it based on the formatting string:
    line_prefix = f"Line {line_num:<4}" 
    # The string above is 4 (Line) + 1 (space) + 4 (number) = 9 characters.
    # The complete prefix is 9 (line_prefix) + 2 ('| ') = 11 characters total.

    # 2. Calculate the pointer padding.
    #    It needs the prefix width (11) PLUS the column number.
    prefix_width = len(line_prefix) + 2  # 'Line 5    ' is 9 chars. The '| ' is 2 chars. Total 11 chars.
    
    # The pointer string starts with enough spaces to align it with the source code.
    # Padding = Prefix Width + Column Number
    pointer_padding = ' ' * prefix_width
    
    # The arrow needs to be placed at the column number offset relative to the code start.
    pointer_line = f"{pointer_padding}{' ' * col_num}^"

    report = [
        f"\n❌ {error_type}: {error_info['message']}",
        f"Located at line {line_num}, column {col_num}:",
        f"{line_prefix}| {source_line}",
        pointer_line
    ]
    return "\n".join(report)

# 1. Custom Error Listener for Syntax Errors
class ErrorReportListener(ErrorListener):
    """Captures and stores syntax errors with line/column information."""
    def __init__(self, source_code):
        super().__init__()
        # Split source code into lines for easy lookup
        self.source_code_lines = source_code.splitlines(keepends=False)
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # ANTLR uses 1-based line and 0-based column.
        try:
            problematic_line = self.source_code_lines[line - 1]
        except IndexError:
            problematic_line = ""

        error_message = f"Syntax Error: {msg}"
        self.errors.append({
            'message': error_message,
            'line': line,
            'column': column,
            'source_line': problematic_line,
            'error_pointer': ' ' * column + '^'
        })

    def report_errors(self):
        return self.errors


# 2. Main Interpreter Class
class Interpreter(ExprVisitor):
    
    # Custom exception to carry error location info
    class CustomRuntimeError(Exception):
        def __init__(self, error_info, *args, **kwargs):
            self.error_info = error_info
            super().__init__(error_info['message'], *args, **kwargs)

    def __init__(self, initial_env=None):
        self.env = initial_env if initial_env is not None else {}
        self.source_code = ""

    # Helper to get error info from a Context object
    def _get_error_info(self, ctx, message):
        """Extracts location information from an ANTLR context or token."""
        # Check if ctx is a Token (e.g., from ctx.ID().getPayload()) or a RuleContext
        if isinstance(ctx, Token):
            start_token = ctx
        else:
            start_token = ctx.start

        # Tokens provide line and column information
        return {
            'message': message,
            'line': start_token.line,
            'column': start_token.column,
            'source_line': self.source_code.splitlines(keepends=False)[start_token.line - 1],
            # Point to the start of the token
            'error_pointer': ' ' * start_token.column + '^'
        }
    
    # NEW: Default error output handler (prints to console)
    def _handle_error_output(self, error_info, error_type):
        """Default error output (prints to standard error)."""
        print(format_error(error_info, error_type), file=sys.stderr)

    # Entry: interpret a whole input string
    def interpret(self, text):
        self.source_code = text
        input_stream = InputStream(text)
        lexer = ExprLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = ExprParser(stream)

        parser.removeErrorListeners()
        error_listener = ErrorReportListener(text)
        parser.addErrorListener(error_listener)
        
        tree = parser.prog()

        # Check for syntax errors first
        syntax_errors = error_listener.report_errors()
        if syntax_errors:
            # CALL 1: Format the syntax error before handling the output
            self._handle_error_output(syntax_errors[0], "Syntax Error")
            return None

        try:
            return self.visit(tree)
        except self.CustomRuntimeError as e:
            # Use the defined error handler
            self._handle_error_output(e.error_info, "Runtime Error")
            return None
    
    # ---- Program ----
    def visitProg(self, ctx: ExprParser.ProgContext):
        result = None
        for stat in ctx.stat():
            result = self.visit(stat)
        return result

    # ---- Statements ----
    def visitAssignment(self, ctx: ExprParser.AssignmentContext):
        var_name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.env[var_name] = value
        return value

    def visitAssertStat(self, ctx: ExprParser.AssertStatContext):
        value = self.visit(ctx.expr())
        if not value:
            message = "Assertion failed."
            # CORRECTED: Use the expression context (ctx.expr()) 
            # to get the location of 'x < 0'
            error_info = self._get_error_info(ctx.expr(), message) 
            raise self.CustomRuntimeError(error_info)
        return value
    
    def visitPrintStat(self, ctx: ExprParser.PrintStatContext):
        value = self.visit(ctx.expr())
        print(value) 
        return value

    def visitStat(self, ctx: ExprParser.StatContext):
        # Could be assignment, expression, or assertStat
        if ctx.assignment():
            return self.visit(ctx.assignment())
        elif ctx.assertStat():
            return self.visit(ctx.assertStat())
        elif ctx.printStat():
            return self.visit(ctx.printStat())
        else:
            return self.visit(ctx.expr())

    # ---- Expressions ----
    def visitExpr(self, ctx: ExprParser.ExprContext):
        return self.visit(ctx.orExpr())

    def visitOrExpr(self, ctx: ExprParser.OrExprContext):
        if len(ctx.OR()) == 0:
            return self.visit(ctx.andExpr(0))
        result = bool(self.visit(ctx.andExpr(0)))
        for i, _ in enumerate(ctx.OR()):
            right = bool(self.visit(ctx.andExpr(i + 1)))
            result = result or right
        return result


    def visitAndExpr(self, ctx: ExprParser.AndExprContext):
        if len(ctx.AND()) == 0:
            return self.visit(ctx.notExpr(0))
        result = bool(self.visit(ctx.notExpr(0)))
        for i, _ in enumerate(ctx.AND()):
            right = bool(self.visit(ctx.notExpr(i + 1)))
            result = result and right
        return result


    def visitNotExpr(self, ctx: ExprParser.NotExprContext):
        if ctx.NOT():
            return not self.visit(ctx.notExpr())
        return self.visit(ctx.cmpExpr())

    def visitCmpExpr(self, ctx: ExprParser.CmpExprContext):
        if len(ctx.COMPARE()) == 0:
            return self.visit(ctx.addSubExpr(0))

        left = self.visit(ctx.addSubExpr(0))
        for i, op in enumerate(ctx.COMPARE()):
            right = self.visit(ctx.addSubExpr(i + 1))
            op_text = op.getText()

            match op_text:
                case '==': ok = left == right
                case '!=': ok = left != right
                case '<':  ok = left < right
                case '<=': ok = left <= right
                case '>':  ok = left > right
                case '>=': ok = left >= right
                case _: raise RuntimeError(f"Unknown comparison operator: {op_text}")

            if not ok:
                return False
            left = right

        return True


    def visitAddSubExpr(self, ctx: ExprParser.AddSubExprContext):
        result = self.visit(ctx.mulDivExpr(0))
        for i, op in enumerate(ctx.ADD_SUB()):
            match op.getText():
                case '+':
                    result += self.visit(ctx.mulDivExpr(i + 1))
                case '-':
                    result -= self.visit(ctx.mulDivExpr(i + 1))
        return result

    def visitMulDivExpr(self, ctx: ExprParser.MulDivExprContext):
        result = self.visit(ctx.unaryExpr(0))
        for i, op in enumerate(ctx.MUL_DIV()):
            right = self.visit(ctx.unaryExpr(i + 1))
            t = op.getText()
            match t:
                case '*':
                    result *= right
                case '/':
                    result /= right
                case '%':
                    result %= right
        return result

    def visitUnaryExpr(self, ctx: ExprParser.UnaryExprContext):
        if ctx.ADD_SUB():
            sign = ctx.ADD_SUB().getText()
            val = self.visit(ctx.unaryExpr())
            return +val if sign == '+' else -val
        return self.visit(ctx.powExpr())

    def visitPowExpr(self, ctx: ExprParser.PowExprContext):
        left = self.visit(ctx.atom())
        if ctx.powExpr():
            right = self.visit(ctx.powExpr())
            return left ** right
        return left

    # ---- Atoms ----
    def visitAtom(self, ctx: ExprParser.AtomContext):
        if ctx.ID():
            var_name = ctx.ID().getText()
            if var_name not in self.env:
                message = f"Undefined variable '{var_name}'."
                error_info = self._get_error_info(ctx.ID().getPayload(), message)
                raise self.CustomRuntimeError(error_info)
            return self.env[var_name]
        # ... (rest of visitAtom)
        if ctx.numberExpr(): return self.visit(ctx.numberExpr())
        if ctx.scientificExpr(): return self.visit(ctx.scientificExpr())
        if ctx.expr(): return self.visit(ctx.expr())
        raise Exception("Unknown atom type")

    def visitNumberExpr(self, ctx: ExprParser.NumberExprContext):
        text = ctx.NUMBER().getText()
        return float(text)

    def visitScientificExpr(self, ctx: ExprParser.ScientificExprContext):
        base = float(ctx.NUMBER().getText())
        # The exponent is the expr() following 'x10^'
        exponent = self.visit(ctx.expr()) 
        return base * (10 ** exponent)


class StreamingInterpreter(Interpreter):
    """An Interpreter subclass that redirects print and error output via callbacks."""
    def __init__(self, initial_env=None):
        super().__init__(initial_env)
        self._stream_callback = None

    def set_stream_callback(self, callback):
        """Set a single callback for both stdout and stderr streaming."""
        self._stream_callback = callback
    
    # OVERRIDE: Redirects print statements to the unified callback
    def visitPrintStat(self, ctx: ExprParser.PrintStatContext):
        value = self.visit(ctx.expr())
        if self._stream_callback:
            # Send structured JSON string for stdout
            self._stream_callback(json.dumps({ 'type': 'stdout', 'content': str(value) }))
        else:
            print(value) 
        return value

    # OVERRIDE: Redirects all error output to the unified callback
    def _handle_error_output(self, error_info, error_type):
        """Streams the formatted error report to the stderr callback."""
        formatted_error = format_error(error_info, error_type)
        
        # Determine the event type based on error_type string
        stream_type = 'syntax_error' if 'Syntax' in error_type else 'runtime_error'
        
        event = json.dumps({
            'type': stream_type, 
            'content': formatted_error
        })
        
        if self._stream_callback:
            # Send structured JSON string for errors
            self._stream_callback(event)
        else:
            super()._handle_error_output(error_info, error_type)

# ---- Example Usage ----
if __name__ == "__main__":
    
    # Example demonstrating a **runtime error** (Undefined variable 'z')
    code_runtime_error = """
a = 10
b = a * 2
assert b == 20
print b + z  # 'z' is undefined, will cause a NameError (caught as CustomRuntimeError)
result = 1
"""
    print("--- Testing Runtime Error (Undefined Variable) ---")
    interpreter_runtime = Interpreter()
    interpreter_runtime.interpret(code_runtime_error)

    print("\n" + "="*50 + "\n")

    # Example demonstrating an **assertion error**
    code_assertion_error = """
x = 5
y = 10
assert x == y # Fails here
print x
"""
    print("--- Testing Runtime Error (Assertion Failure) ---")
    interpreter_assert = Interpreter()
    interpreter_assert.interpret(code_assertion_error)

    print("\n" + "="*50 + "\n")

    # Example demonstrating a **syntax error** (Requires actual ExprParser/Lexer to trigger)
    # The '3x10^y' syntax is likely what you defined with your scientificExpr rule. 
    # Let's assume an error where 'result' is missing an operator.
    code_syntax_error = """
z = 1 + 2
result x * 3  # Missing assignment operator '='
y = 10
"""
    print("--- Testing Syntax Error (Assuming Missing '=') ---")
    # For demonstration, since I can't run ANTLR, I'll simulate the output 
    # that the ErrorReportListener *should* produce if run on this code:
    
    # interpreter_syntax = Interpreter()
    # interpreter_syntax.interpret(code_syntax_error)
    
    # Simulated Syntax Error Output:
    simulated_syntax_error = {
        'message': "mismatched input 'x' expecting {EOL, ';', '+', '-', '*', ...}",
        'line': 3,
        'column': 7,
        'source_line': 'result x * 3  # Missing assignment operator \'=\'',
        'error_pointer': ' ' * 7 + '^'
    }
    print(format_error(simulated_syntax_error, "Syntax Error"))