import cov_lexer
import cov_parser
import cov_interpreter

from sys import *

#MASUKAN LANGSUNG
if __name__ == '__main__':
    lexer = cov_lexer.BasicLexer()
    parser = cov_parser.BasicParser()
    env = {}
    while True:
        try:
            text = input('cov > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            cov_interpreter.BasicExecute(tree, env)
