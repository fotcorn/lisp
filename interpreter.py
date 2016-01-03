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
        elif isinstance(value, Identifier):
            if value.value in self.variables:
                return self.variables[value.value]
            else:
                raise Exception(u'Unknown variable {}'.format(value.value))
        elif isinstance(value, Call):
            operator = value.expressions[0]

            if operator.value == 'def':
                if not len(value.expressions) == 3:
                    raise Exception(u'def takes exactly two arguments')
                if not isinstance(value.expressions[1], Identifier):
                    raise Exception(u'The first argument of def must be an identifier')
                variable_value = self.evaluate(value.expressions[2])
                variable_name = value.expressions[1].value
                self.variables[variable_name] = variable_value
                return

            values = []
            for param in value.expressions[1:]:
                values.append(self.evaluate(param))

            if isinstance(operator, Identifier):
                if operator.value in self.builtins:
                    builtin = self.builtins[operator.value]
                    return builtin(self, values)
                elif operator.value in self.variables:
                    variable = self.variables[operator.value]
                    if variable.type != Value.FUNCTION:
                        raise Exception(u'Trying to call non-function value: {}'.format(variable))
                else:
                    raise Exception(u'Trying to call unknown function: {}'.format(operator.value))
            elif isinstance(operator, Function):
                pass  # TODO: execute function
            else:
                raise Exception(u'Trying to execute non-function as function')


def run(ast):
    interpreter = Interpreter(ast, interpreter_builtins.builtins)
    interpreter.run()
