import codecs

from lexer import lex
from parser import parse
# from interpreter import run

if __name__ == '__main__':
    with codecs.open('example.lisp', encoding='utf-8') as f:
        program = f.read().strip()
    tokens = lex(program)

    ast = parse(tokens)
    for expression in ast:
        print expression.expressions
    # run(ast)
