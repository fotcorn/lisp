import sys

import readline

from lisp import interpreter_builtins
from lisp.interpreter_exceptions import InterpreterException
from lisp.lexer import lex, LexerException
from lisp.parser import parse, ParseError
from lisp.interpreter import run, Interpreter


def repl():
    print("Write 'exit' to exit repl")

    readline.parse_and_bind('')

    interpreter = Interpreter(interpreter_builtins.builtins)

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
            value = interpreter.run(ast)
            if value:
                print(value)
        except (LexerException, ParseError, InterpreterException) as ex:
            print('Error: ', str(ex))