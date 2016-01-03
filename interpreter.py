from interpreter_value import Value
from parser import Identifier, Function, Number, String, Call
import interpreter_builtins


class Interpreter(object):

    def __init__(self, ast, builtins):
        self.variables = {}
        self.builtins = builtins
        self.ast = ast

    def run(self):
        for expression in self.ast:
            self.evaluate(expression)

    def evaluate(self, value):
        if isinstance(value, Number):
            return Value(Value.INTEGER, value.value)
        elif isinstance(value, String):
            return Value(Value.STRING, value.value)
        elif isinstance(value, Function):
            return Value(Value.FUNCTION, value)
        elif isinstance(value, Call):
            values = []
            for param in value.expressions[1:]:
                values.append(self.evaluate(param))

            operator = value.expressions[0]
            if isinstance(operator, Identifier):
                if operator.value in self.builtins:
                    builtin = self.builtins[operator.value]
                    return builtin(self, values)
                pass  # TODO: check variables
            elif isinstance(operator, Function):
                pass  # TODO: execute function


def run(ast):
    interpreter = Interpreter(ast, interpreter_builtins.builtins)
    interpreter.run()
