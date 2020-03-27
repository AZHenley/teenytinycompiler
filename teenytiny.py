import enum

def main():
    # Read.
    # Lex.
    # Parse.
    # Generate.
    # Write.
    pass

def abort():
    pass


# Lexer.

class Lexer:
    def currentTokenIs(self, token):
        pass

    def consume(self, token):
        pass


# Token.
class Token(enum.Enum):
    NUMBER = 1
    IDENT = 2
    # Keywords.
    LABEL = 3
    GOTO = 4
    PRINT = 5
    INPUT = 6
    LET = 7
    IF = 8
    THEN = 9
    ENDIF = 10
    WHILE = 11
    ENDWHILE = 12
    # Operators.
    OP_EQ = 13  
    OP_PLUS = 14
    OP_MINUS = 15
    OP_MULT = 16
    OP_DIV = 17
    OP_EQEQ = 18
    OP_NOTEQ = 19
    OP_LT = 20
    OP_LTEQ = 21
    OP_GT = 22
    OP_GTEQ = 23

class Emitter():
    pass



