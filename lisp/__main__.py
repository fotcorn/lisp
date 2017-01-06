import os
import sys

from lisp.interpreter import run
from lisp.lexer import lex
from lisp.parser import parse
from lisp.repl import repl

if __name__ == '__main__':
    if len(sys.argv) not in (1, 2):
        print('Run file:   python -m lisp <file.lisp>')
        print('Start repl: python -m lisp')
        sys.exit(1)

    if len(sys.argv) == 1:
        repl()
    else:
        filename = sys.argv[1]
        if not os.path.exists(filename):
            print('Source file {} does not exist'.format(filename))
            sys.exit(1)

        with open(filename, encoding='utf-8') as f:
            program = f.read().strip()
        tokens = lex(program)
        ast = parse(tokens)
        run(ast)
