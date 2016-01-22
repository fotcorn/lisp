import os
import sys
import codecs

from lisp.lexer import lex
from lisp.parser import parse
from lisp.interpreter import run

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python -m lisp <file.lisp>')
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.exists(filename):
        print('Source file {} does not exist'.format(filename))
        sys.exit(1)

    with codecs.open(filename, encoding='utf-8') as f:
        program = f.read().strip()
    tokens = lex(program)

    ast = parse(tokens)
    run(ast)
