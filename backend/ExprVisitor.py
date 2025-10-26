# Generated from Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx:ExprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#stat.
    def visitStat(self, ctx:ExprParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assignment.
    def visitAssignment(self, ctx:ExprParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assertStat.
    def visitAssertStat(self, ctx:ExprParser.AssertStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#printStat.
    def visitPrintStat(self, ctx:ExprParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expr.
    def visitExpr(self, ctx:ExprParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#orExpr.
    def visitOrExpr(self, ctx:ExprParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#andExpr.
    def visitAndExpr(self, ctx:ExprParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#notExpr.
    def visitNotExpr(self, ctx:ExprParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#cmpExpr.
    def visitCmpExpr(self, ctx:ExprParser.CmpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#addSubExpr.
    def visitAddSubExpr(self, ctx:ExprParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mulDivExpr.
    def visitMulDivExpr(self, ctx:ExprParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#unaryExpr.
    def visitUnaryExpr(self, ctx:ExprParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#powExpr.
    def visitPowExpr(self, ctx:ExprParser.PowExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#atom.
    def visitAtom(self, ctx:ExprParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#numberExpr.
    def visitNumberExpr(self, ctx:ExprParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#scientificExpr.
    def visitScientificExpr(self, ctx:ExprParser.ScientificExprContext):
        return self.visitChildren(ctx)



del ExprParser