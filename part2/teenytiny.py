from lex import *
from parse import *
import sys

def main():
    input = "LET a = 5 \n LET b = a * 3 \n PRINT a + b" # Testing

    # Initialize the lexer and parser.
    lexer = Lexer(input)
    parser = Parser(lexer)

    parser.program() # Start the parser.
    print("Parsing completed.")

main()
