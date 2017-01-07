import os
import sys
import readline
import atexit

from lisp import interpreter_builtins
from lisp.interpreter_exceptions import InterpreterException
from lisp.lexer import lex, LexerException
from lisp.parser import parse, ParseError
from lisp.interpreter import run, Interpreter


def repl():
    print("Write 'exit' to exit repl")

    history_file = os.path.join(os.path.expanduser("~"), ".fotcorn_lisp_history")
    try:
        readline.read_history_file(history_file)
        readline.set_history_length(1000)
    except FileNotFoundError:
        pass
    atexit.register(readline.write_history_file, history_file)

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
