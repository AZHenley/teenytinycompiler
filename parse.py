import sys
from lex import *

# Parser object keeps track of current token, checks if the code matches the grammar, and emits code along the way.
class Parser:
    def __init__(self, lexer, emitter):
        self.lexer = lexer
        self.emitter = emitter
        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()    # Call this twice to initialize current and peek.

    # Return true if the current token matches.
    def checkToken(self, kind):
        return kind == self.curToken.kind

    # Return true if the next token matches.
    def checkPeek(self, kind):
        return kind == self.peekToken.kind

    # Try to match current token. If not, error. Advances the current token.
    def match(self, kind):
        if not self.checkToken(kind):
            self.abort("Expected " + kind.name + ", got " + self.curToken.kind.name)
        self.nextToken()

    # Advances the current token.
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()
        # No need to worry about passing the EOF, lexer handles that.

    def abort(self, message):
        print("Parsing error. " + message)
        sys.exit()


    # Production rules.

    # program ::= {statement '\n'}
    def program(self):
        self.emitter.emitLine("#include <stdio.h>")
        self.emitter.emitLine("int main(void){")
        
        while not self.checkToken(TokenType.EOF):
            self.statement()
            self.match(TokenType.NEWLINE)

        self.emitter.emitLine("return 0;")
        self.emitter.emitLine("}")

    # One of the following statements...
    def statement(self):
        # Check the first token to see what kind of statement this is.

        # "PRINT" expression
        if self.checkToken(TokenType.PRINT):
            self.nextToken()
            self.expression()
        # "IF" comparison "THEN" block "ENDIF"
        elif self.checkToken(TokenType.IF):
            self.nextToken()
            self.comparison()
            self.match(TokenType.THEN)
            while not self.checkToken(TokenType.ENDIF):
                self.statement()
                self.match(TokenType.NEWLINE)
            self.match(TokenType.ENDIF)
        # "WHILE" comparison "REPEAT" block "ENDWHILE"
        elif self.checkToken(TokenType.WHILE):
            self.nextToken()
            self.comparison()
            self.match(TokenType.REPEAT)
            while not self.checkToken(TokenType.ENDWHILE):
                self.statement()
                self.match(TokenType.NEWLINE)
            self.match(TokenType.ENDWHILE)
        # "LABEL" ident
        elif self.checkToken(TokenType.LABEL):
            self.nextToken()
            self.match(TokenType.IDENT)
        # "GOTO" ident
        elif self.checkToken(TokenType.GOTO):
            self.nextToken()
            self.match(TokenType.IDENT)
        # "LET" ident = expression
        elif self.checkToken(TokenType.LET):
            self.nextToken()
            self.match(TokenType.IDENT)
        # "INPUT" ident
        elif self.checkToken(TokenType.INPUT):
            self.nextToken()
            self.match(TokenType.IDENT)
        # This is not a valid statement. Error!
        else:
            self.abort("Invalid statement at " + self.curToken.text)

    # comparison ::= expression (("==" | "!=" | ">" | ">=" | "<" | "<=") expression)+
    def comparison(self):
        self.expression()
        # Must be at least one comparison operator and another expression.
        if self.checkToken(TokenType.GT) or self.checkToken(TokenType.GTEQ) or self.checkToken(TokenType.LT) or self.checkToken(TokenType.LTEQ):
            self.nextToken()
            self.expression()
        # Can have 0 or more comparison operator and expressions.
        while self.checkToken(TokenType.GT) or self.checkToken(TokenType.GTEQ) or self.checkToken(TokenType.LT) or self.checkToken(TokenType.LTEQ):
            self.nextToken()
            self.expression()

    # expression ::= term {( "-" | "+" ) term}
    def expression(self):
        self.term()
        # Can have 0 or more +/- and expressions.
        while self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            self.nextToken()
            self.term()

    # term ::= unary {( "/" | "*" ) unary}
    def term(self):
        self.unary()
        # Can have 0 or more *// and expressions.
        while self.checkToken(TokenType.ASTERISK) or self.checkToken(TokenType.SLASH):
            self.nextToken()
            self.unary()

    # unary ::= ["+" | "-"] primary
    def unary(self):
        # Optional unary +/-
        if self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            self.nextToken()        
        self.primary()

    # primary ::= number | ident
    def primary(self):
        if self.checkToken(TokenType.NUMBER) or self.checkToken(TokenType.IDENT):
            self.nextToken()
        else:
            # Error!
            self.abort("Unexpected token at " + self.curToken.text)