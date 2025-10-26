# Generated from Expr.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,131,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,4,0,36,8,0,11,0,12,0,37,1,0,3,
        0,41,8,0,1,1,1,1,1,1,1,1,3,1,47,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,
        1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,5,6,64,8,6,10,6,12,6,67,9,6,1,7,
        1,7,1,7,5,7,72,8,7,10,7,12,7,75,9,7,1,8,1,8,1,8,3,8,80,8,8,1,9,1,
        9,1,9,5,9,85,8,9,10,9,12,9,88,9,9,1,10,1,10,1,10,5,10,93,8,10,10,
        10,12,10,96,9,10,1,11,1,11,1,11,5,11,101,8,11,10,11,12,11,104,9,
        11,1,12,1,12,1,12,3,12,109,8,12,1,13,1,13,1,13,3,13,114,8,13,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,3,14,123,8,14,1,15,1,15,1,16,1,16,
        1,16,1,16,1,16,0,0,17,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,0,0,129,0,40,1,0,0,0,2,46,1,0,0,0,4,48,1,0,0,0,6,52,1,0,0,0,8,
        55,1,0,0,0,10,58,1,0,0,0,12,60,1,0,0,0,14,68,1,0,0,0,16,79,1,0,0,
        0,18,81,1,0,0,0,20,89,1,0,0,0,22,97,1,0,0,0,24,108,1,0,0,0,26,110,
        1,0,0,0,28,122,1,0,0,0,30,124,1,0,0,0,32,126,1,0,0,0,34,36,3,2,1,
        0,35,34,1,0,0,0,36,37,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,41,
        1,0,0,0,39,41,5,0,0,1,40,35,1,0,0,0,40,39,1,0,0,0,41,1,1,0,0,0,42,
        47,3,4,2,0,43,47,3,10,5,0,44,47,3,6,3,0,45,47,3,8,4,0,46,42,1,0,
        0,0,46,43,1,0,0,0,46,44,1,0,0,0,46,45,1,0,0,0,47,3,1,0,0,0,48,49,
        5,14,0,0,49,50,5,1,0,0,50,51,3,10,5,0,51,5,1,0,0,0,52,53,5,5,0,0,
        53,54,3,10,5,0,54,7,1,0,0,0,55,56,5,6,0,0,56,57,3,10,5,0,57,9,1,
        0,0,0,58,59,3,12,6,0,59,11,1,0,0,0,60,65,3,14,7,0,61,62,5,7,0,0,
        62,64,3,14,7,0,63,61,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,
        0,0,0,66,13,1,0,0,0,67,65,1,0,0,0,68,73,3,16,8,0,69,70,5,8,0,0,70,
        72,3,16,8,0,71,69,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,
        0,0,74,15,1,0,0,0,75,73,1,0,0,0,76,77,5,9,0,0,77,80,3,16,8,0,78,
        80,3,18,9,0,79,76,1,0,0,0,79,78,1,0,0,0,80,17,1,0,0,0,81,86,3,20,
        10,0,82,83,5,13,0,0,83,85,3,20,10,0,84,82,1,0,0,0,85,88,1,0,0,0,
        86,84,1,0,0,0,86,87,1,0,0,0,87,19,1,0,0,0,88,86,1,0,0,0,89,94,3,
        22,11,0,90,91,5,11,0,0,91,93,3,22,11,0,92,90,1,0,0,0,93,96,1,0,0,
        0,94,92,1,0,0,0,94,95,1,0,0,0,95,21,1,0,0,0,96,94,1,0,0,0,97,102,
        3,24,12,0,98,99,5,12,0,0,99,101,3,24,12,0,100,98,1,0,0,0,101,104,
        1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,23,1,0,0,0,104,102,1,
        0,0,0,105,106,5,11,0,0,106,109,3,24,12,0,107,109,3,26,13,0,108,105,
        1,0,0,0,108,107,1,0,0,0,109,25,1,0,0,0,110,113,3,28,14,0,111,112,
        5,10,0,0,112,114,3,26,13,0,113,111,1,0,0,0,113,114,1,0,0,0,114,27,
        1,0,0,0,115,123,3,30,15,0,116,123,3,32,16,0,117,118,5,2,0,0,118,
        119,3,10,5,0,119,120,5,3,0,0,120,123,1,0,0,0,121,123,5,14,0,0,122,
        115,1,0,0,0,122,116,1,0,0,0,122,117,1,0,0,0,122,121,1,0,0,0,123,
        29,1,0,0,0,124,125,5,15,0,0,125,31,1,0,0,0,126,127,5,15,0,0,127,
        128,5,4,0,0,128,129,3,10,5,0,129,33,1,0,0,0,12,37,40,46,65,73,79,
        86,94,102,108,113,122
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "'x10^'", "'assert'", 
                     "'print'", "'or'", "'and'", "'not'", "'^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ASSERT", "PRINT", "OR", "AND", "NOT", 
                      "POW", "ADD_SUB", "MUL_DIV", "COMPARE", "ID", "NUMBER", 
                      "COMMENT", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_assignment = 2
    RULE_assertStat = 3
    RULE_printStat = 4
    RULE_expr = 5
    RULE_orExpr = 6
    RULE_andExpr = 7
    RULE_notExpr = 8
    RULE_cmpExpr = 9
    RULE_addSubExpr = 10
    RULE_mulDivExpr = 11
    RULE_unaryExpr = 12
    RULE_powExpr = 13
    RULE_atom = 14
    RULE_numberExpr = 15
    RULE_scientificExpr = 16

    ruleNames =  [ "prog", "stat", "assignment", "assertStat", "printStat", 
                   "expr", "orExpr", "andExpr", "notExpr", "cmpExpr", "addSubExpr", 
                   "mulDivExpr", "unaryExpr", "powExpr", "atom", "numberExpr", 
                   "scientificExpr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    ASSERT=5
    PRINT=6
    OR=7
    AND=8
    NOT=9
    POW=10
    ADD_SUB=11
    MUL_DIV=12
    COMPARE=13
    ID=14
    NUMBER=15
    COMMENT=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatContext,i)


        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 5, 6, 9, 11, 14, 15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 34
                    self.stat()
                    self.state = 37 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 51812) != 0)):
                        break

                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.match(ExprParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(ExprParser.AssignmentContext,0)


        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def assertStat(self):
            return self.getTypedRuleContext(ExprParser.AssertStatContext,0)


        def printStat(self):
            return self.getTypedRuleContext(ExprParser.PrintStatContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = ExprParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.assertStat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.printStat()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = ExprParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(ExprParser.ID)
            self.state = 49
            self.match(ExprParser.T__0)
            self.state = 50
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssertStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSERT(self):
            return self.getToken(ExprParser.ASSERT, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_assertStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssertStat" ):
                listener.enterAssertStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssertStat" ):
                listener.exitAssertStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssertStat" ):
                return visitor.visitAssertStat(self)
            else:
                return visitor.visitChildren(self)




    def assertStat(self):

        localctx = ExprParser.AssertStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assertStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(ExprParser.ASSERT)
            self.state = 53
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(ExprParser.PRINT, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_printStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStat" ):
                listener.enterPrintStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStat" ):
                listener.exitPrintStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStat" ):
                return visitor.visitPrintStat(self)
            else:
                return visitor.visitChildren(self)




    def printStat(self):

        localctx = ExprParser.PrintStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_printStat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(ExprParser.PRINT)
            self.state = 56
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def orExpr(self):
            return self.getTypedRuleContext(ExprParser.OrExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.orExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.AndExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.AndExprContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.OR)
            else:
                return self.getToken(ExprParser.OR, i)

        def getRuleIndex(self):
            return ExprParser.RULE_orExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)




    def orExpr(self):

        localctx = ExprParser.OrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_orExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.andExpr()
            self.state = 65
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 61
                    self.match(ExprParser.OR)
                    self.state = 62
                    self.andExpr() 
                self.state = 67
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def notExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.NotExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.NotExprContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.AND)
            else:
                return self.getToken(ExprParser.AND, i)

        def getRuleIndex(self):
            return ExprParser.RULE_andExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)




    def andExpr(self):

        localctx = ExprParser.AndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_andExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.notExpr()
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 69
                    self.match(ExprParser.AND)
                    self.state = 70
                    self.notExpr() 
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NotExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ExprParser.NOT, 0)

        def notExpr(self):
            return self.getTypedRuleContext(ExprParser.NotExprContext,0)


        def cmpExpr(self):
            return self.getTypedRuleContext(ExprParser.CmpExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_notExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)




    def notExpr(self):

        localctx = ExprParser.NotExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_notExpr)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(ExprParser.NOT)
                self.state = 77
                self.notExpr()
                pass
            elif token in [2, 11, 14, 15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 78
                self.cmpExpr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmpExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def addSubExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.AddSubExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.AddSubExprContext,i)


        def COMPARE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMPARE)
            else:
                return self.getToken(ExprParser.COMPARE, i)

        def getRuleIndex(self):
            return ExprParser.RULE_cmpExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmpExpr" ):
                listener.enterCmpExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmpExpr" ):
                listener.exitCmpExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmpExpr" ):
                return visitor.visitCmpExpr(self)
            else:
                return visitor.visitChildren(self)




    def cmpExpr(self):

        localctx = ExprParser.CmpExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cmpExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.addSubExpr()
            self.state = 86
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 82
                    self.match(ExprParser.COMPARE)
                    self.state = 83
                    self.addSubExpr() 
                self.state = 88
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddSubExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mulDivExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.MulDivExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.MulDivExprContext,i)


        def ADD_SUB(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ADD_SUB)
            else:
                return self.getToken(ExprParser.ADD_SUB, i)

        def getRuleIndex(self):
            return ExprParser.RULE_addSubExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)




    def addSubExpr(self):

        localctx = ExprParser.AddSubExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_addSubExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.mulDivExpr()
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 90
                    self.match(ExprParser.ADD_SUB)
                    self.state = 91
                    self.mulDivExpr() 
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MulDivExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.UnaryExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.UnaryExprContext,i)


        def MUL_DIV(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.MUL_DIV)
            else:
                return self.getToken(ExprParser.MUL_DIV, i)

        def getRuleIndex(self):
            return ExprParser.RULE_mulDivExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)




    def mulDivExpr(self):

        localctx = ExprParser.MulDivExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_mulDivExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.unaryExpr()
            self.state = 102
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 98
                    self.match(ExprParser.MUL_DIV)
                    self.state = 99
                    self.unaryExpr() 
                self.state = 104
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self):
            return self.getTypedRuleContext(ExprParser.UnaryExprContext,0)


        def ADD_SUB(self):
            return self.getToken(ExprParser.ADD_SUB, 0)

        def powExpr(self):
            return self.getTypedRuleContext(ExprParser.PowExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_unaryExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = ExprParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_unaryExpr)
        try:
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.match(ExprParser.ADD_SUB)
                self.state = 106
                self.unaryExpr()
                pass
            elif token in [2, 14, 15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.powExpr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PowExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(ExprParser.AtomContext,0)


        def POW(self):
            return self.getToken(ExprParser.POW, 0)

        def powExpr(self):
            return self.getTypedRuleContext(ExprParser.PowExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_powExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowExpr" ):
                listener.enterPowExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowExpr" ):
                listener.exitPowExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPowExpr" ):
                return visitor.visitPowExpr(self)
            else:
                return visitor.visitChildren(self)




    def powExpr(self):

        localctx = ExprParser.PowExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_powExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.atom()
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 111
                self.match(ExprParser.POW)
                self.state = 112
                self.powExpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numberExpr(self):
            return self.getTypedRuleContext(ExprParser.NumberExprContext,0)


        def scientificExpr(self):
            return self.getTypedRuleContext(ExprParser.ScientificExprContext,0)


        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = ExprParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_atom)
        try:
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                self.numberExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 116
                self.scientificExpr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 117
                self.match(ExprParser.T__1)
                self.state = 118
                self.expr()
                self.state = 119
                self.match(ExprParser.T__2)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 121
                self.match(ExprParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ExprParser.NUMBER, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_numberExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)




    def numberExpr(self):

        localctx = ExprParser.NumberExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_numberExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(ExprParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScientificExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ExprParser.NUMBER, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_scientificExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScientificExpr" ):
                listener.enterScientificExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScientificExpr" ):
                listener.exitScientificExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScientificExpr" ):
                return visitor.visitScientificExpr(self)
            else:
                return visitor.visitChildren(self)




    def scientificExpr(self):

        localctx = ExprParser.ScientificExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_scientificExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(ExprParser.NUMBER)
            self.state = 127
            self.match(ExprParser.T__3)
            self.state = 128
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





