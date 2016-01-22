import unittest
from StringIO import StringIO

from lisp import interpreter_builtins
from lisp.interpreter import Interpreter
from lisp.lexer import lex
from lisp.parser import parse


class BaseTestCase(unittest.TestCase):
    def assert_stdout(self, program, stdout):
        tokens = lex(program)
        ast = parse(tokens)

        stdout_file = StringIO()
        interpreter = Interpreter(ast, interpreter_builtins.builtins, stdout=stdout_file)
        interpreter.run()

        self.assertEqual(stdout_file.getvalue(), stdout)

    def assert_exception(self, program, exception_type):
        tokens = lex(program)
        ast = parse(tokens)

        interpreter = Interpreter(ast, interpreter_builtins.builtins)
        self.assertRaises(exception_type, interpreter.run)
