import cov_lexer
import cov_parser
import cov_interpreter

from sys import *

lexer = cov_lexer.BasicLexer()
parser = cov_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    cov_interpreter.BasicExecute(tree, env)
