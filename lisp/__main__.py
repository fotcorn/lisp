import os
import sys

import readline

from lisp.interpreter_exceptions import InterpreterException
from lisp.lexer import lex, LexerException
from lisp.parser import parse, ParseError
from lisp.interpreter import run

if __name__ == '__main__':
    if len(sys.argv) not in (1, 2):
        print('Run file:   python -m lisp <file.lisp>')
        print('Start repl: python -m lisp')
        sys.exit(1)

    if len(sys.argv) == 1:
        print("Write 'exit' to exit repl")

        readline.parse_and_bind('')
        while True:
            try:
                line = input('>>> ')
            except EOFError:
                sys.exit(0)
            except KeyboardInterrupt:
                print()
                continue
            if line == 'exit':
                sys.exit(0)
            try:
                tokens = lex(line)
                ast = parse(tokens)
                run(ast)
            except (LexerException, ParseError, InterpreterException) as ex:
                print('Error: ', str(ex))
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
