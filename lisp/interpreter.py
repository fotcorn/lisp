import sys

from lisp import interpreter_builtins
from lisp.interpreter_exceptions import InterpreterException
from lisp.interpreter_value import Value
from lisp.parser import Identifier, Function, Number, String, Call


class Interpreter(object):

    def __init__(self, builtins, stdout=sys.stdout):
        self.variables = {}
        self.builtins = builtins
        self.stdout = stdout

    def run(self, ast):
        value = None
        for expression in ast:
            value = self.evaluate(expression, {})
        return value

    def evaluate(self, value, variable_context):
        if isinstance(value, Number):
            return Value(Value.INTEGER, value.value)
        elif isinstance(value, String):
            return Value(Value.STRING, value.value)
        elif isinstance(value, Function):
            return Value(Value.FUNCTION, value, variable_context)
        elif isinstance(value, Identifier):
            if value.value == 'true':
                return Value(Value.BOOLEAN, True)
            elif value.value == 'false':
                return Value(Value.BOOLEAN, False)
            elif value.value in variable_context:
                return variable_context[value.value]
            elif value.value in self.variables:
                return self.variables[value.value]
            else:
                raise InterpreterException('Unknown variable {}'.format(value.value))
        elif isinstance(value, Call):
            operator = value.expressions[0]

            if isinstance(operator, Function):
                values = []
                for param in value.expressions[1:]:
                    values.append(self.evaluate(param, variable_context))
                return self.function(operator, values, variable_context)

            if operator.value == 'def':
                if not len(value.expressions) == 3:
                    raise InterpreterException('def takes exactly two arguments')
                if not isinstance(value.expressions[1], Identifier):
                    raise InterpreterException('The first argument of def must be an identifier')
                variable_value = self.evaluate(value.expressions[2], variable_context)
                variable_name = value.expressions[1].value
                self.variables[variable_name] = variable_value
                return

            values = []
            for param in value.expressions[1:]:
                values.append(self.evaluate(param, variable_context))

            if isinstance(operator, Identifier):
                if operator.value in self.builtins:
                    builtin = self.builtins[operator.value]
                    return builtin(self, values)
                elif operator.value in self.variables:
                    variable = self.variables[operator.value]
                    if variable.type != Value.FUNCTION:
                        raise InterpreterException('Trying to call non-function value: {}'.format(variable))
                    func_context = variable_context.copy()
                    func_context.update(variable.variable_context)
                    return self.function(variable.value, values, func_context)
                else:
                    raise InterpreterException('Trying to call unknown function: {}'.format(operator.value))
            else:
                raise InterpreterException('Trying to execute non-function as function')

    def function(self, func, params, variable_context):
        if len(func.param_names) != len(params):
            raise InterpreterException('Argument count does not match')

        variable_context = variable_context.copy()
        for param_name, param_value in zip(func.param_names, params):
            variable_context[param_name] = param_value

        return self.evaluate(func.expression, variable_context)


def run(ast):
    interpreter = Interpreter(interpreter_builtins.builtins)
    return interpreter.run(ast)
