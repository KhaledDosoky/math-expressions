# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#stat.
    def enterStat(self, ctx:ExprParser.StatContext):
        pass

    # Exit a parse tree produced by ExprParser#stat.
    def exitStat(self, ctx:ExprParser.StatContext):
        pass


    # Enter a parse tree produced by ExprParser#assignment.
    def enterAssignment(self, ctx:ExprParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ExprParser#assignment.
    def exitAssignment(self, ctx:ExprParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ExprParser#assertStat.
    def enterAssertStat(self, ctx:ExprParser.AssertStatContext):
        pass

    # Exit a parse tree produced by ExprParser#assertStat.
    def exitAssertStat(self, ctx:ExprParser.AssertStatContext):
        pass


    # Enter a parse tree produced by ExprParser#printStat.
    def enterPrintStat(self, ctx:ExprParser.PrintStatContext):
        pass

    # Exit a parse tree produced by ExprParser#printStat.
    def exitPrintStat(self, ctx:ExprParser.PrintStatContext):
        pass


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx:ExprParser.ExprContext):
        pass

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx:ExprParser.ExprContext):
        pass


    # Enter a parse tree produced by ExprParser#orExpr.
    def enterOrExpr(self, ctx:ExprParser.OrExprContext):
        pass

    # Exit a parse tree produced by ExprParser#orExpr.
    def exitOrExpr(self, ctx:ExprParser.OrExprContext):
        pass


    # Enter a parse tree produced by ExprParser#andExpr.
    def enterAndExpr(self, ctx:ExprParser.AndExprContext):
        pass

    # Exit a parse tree produced by ExprParser#andExpr.
    def exitAndExpr(self, ctx:ExprParser.AndExprContext):
        pass


    # Enter a parse tree produced by ExprParser#notExpr.
    def enterNotExpr(self, ctx:ExprParser.NotExprContext):
        pass

    # Exit a parse tree produced by ExprParser#notExpr.
    def exitNotExpr(self, ctx:ExprParser.NotExprContext):
        pass


    # Enter a parse tree produced by ExprParser#cmpExpr.
    def enterCmpExpr(self, ctx:ExprParser.CmpExprContext):
        pass

    # Exit a parse tree produced by ExprParser#cmpExpr.
    def exitCmpExpr(self, ctx:ExprParser.CmpExprContext):
        pass


    # Enter a parse tree produced by ExprParser#addSubExpr.
    def enterAddSubExpr(self, ctx:ExprParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by ExprParser#addSubExpr.
    def exitAddSubExpr(self, ctx:ExprParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by ExprParser#mulDivExpr.
    def enterMulDivExpr(self, ctx:ExprParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by ExprParser#mulDivExpr.
    def exitMulDivExpr(self, ctx:ExprParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by ExprParser#unaryExpr.
    def enterUnaryExpr(self, ctx:ExprParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by ExprParser#unaryExpr.
    def exitUnaryExpr(self, ctx:ExprParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by ExprParser#powExpr.
    def enterPowExpr(self, ctx:ExprParser.PowExprContext):
        pass

    # Exit a parse tree produced by ExprParser#powExpr.
    def exitPowExpr(self, ctx:ExprParser.PowExprContext):
        pass


    # Enter a parse tree produced by ExprParser#atom.
    def enterAtom(self, ctx:ExprParser.AtomContext):
        pass

    # Exit a parse tree produced by ExprParser#atom.
    def exitAtom(self, ctx:ExprParser.AtomContext):
        pass


    # Enter a parse tree produced by ExprParser#numberExpr.
    def enterNumberExpr(self, ctx:ExprParser.NumberExprContext):
        pass

    # Exit a parse tree produced by ExprParser#numberExpr.
    def exitNumberExpr(self, ctx:ExprParser.NumberExprContext):
        pass


    # Enter a parse tree produced by ExprParser#scientificExpr.
    def enterScientificExpr(self, ctx:ExprParser.ScientificExprContext):
        pass

    # Exit a parse tree produced by ExprParser#scientificExpr.
    def exitScientificExpr(self, ctx:ExprParser.ScientificExprContext):
        pass



del ExprParser