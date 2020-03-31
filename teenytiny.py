from lex import *
from emit import *
from parse import *
import sys

def main():
    print("Teeny Tiny Compiler")

    if len(sys.argv) != 2:
        print("Error: Compiler needs source file as argument.")
        return
    with open(sys.argv[1], 'r') as inputFile:
        input = inputFile.read()
    # input = "LET a = 5 \n LET b = a * 3 \n PRINT a + b" # Testing

    # Initialize the lexer, emitter, and parser.
    lexer = Lexer(input)
    emitter = Emitter("out.c")
    parser = Parser(lexer, emitter)

    parser.program() # Start the parser.
    emitter.writeFile() # Write the output to file.
    print("Compiling completed.")

main()
