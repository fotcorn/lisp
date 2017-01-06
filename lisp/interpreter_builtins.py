from __future__ import print_function

from lisp.interpreter_exceptions import NotEnoughParametersException, UnsupportedParameterType, \
    TooManyParametersException
from lisp.interpreter_value import Value


def plus(interpreter, values):
    if len(values) == 0:
        raise NotEnoughParametersException('+ requires at least one parameter')
    plus_sum = 0
    for value in values:
        if not value.type == Value.INTEGER:
            raise UnsupportedParameterType('+ operator: unsupported operand: {}'.format(value))
        plus_sum += value.value
    return Value(Value.INTEGER, plus_sum)


def minus(interpreter, values):
    if len(values) == 0:
        raise NotEnoughParametersException('- requires at least one parameter')
    if values[0].type != Value.INTEGER:
        raise UnsupportedParameterType('- operator: unsupported operand: {}'.format(values[0].value))
    minus_sum = values[0].value
    if len(values) == 1:
        minus_sum = - minus_sum
    else:
        for value in values[1:]:
            if not value.type == Value.INTEGER:
                raise UnsupportedParameterType('- operator: unsupported operand: {}'.format(value))
            minus_sum -= value.value
    return Value(Value.INTEGER, minus_sum)


def mul(interpreter, values):
    if len(values) == 0:
        raise NotEnoughParametersException('* requires at least one parameter')
    if values[0].type != Value.INTEGER:
        raise UnsupportedParameterType('- operator: unsupported operand: {}'.format(values[0].value))
    mul_sum = values[0].value
    for value in values[1:]:
        if not value.type == Value.INTEGER:
            raise UnsupportedParameterType('* operator: unsupported operand: {}'.format(value))
        mul_sum *= value.value
    return Value(Value.INTEGER, mul_sum)


def div(interpreter, values):
    if len(values) == 0:
        raise NotEnoughParametersException('/ requires at least one parameter')
    if values[0].type != Value.INTEGER:
        raise UnsupportedParameterType('- operator: unsupported operand: {}'.format(values[0].value))
    div_sum = values[0].value
    for value in values[1:]:
        if not value.type == Value.INTEGER:
            raise UnsupportedParameterType('/ operator: unsupported operand: {}'.format(value))
        div_sum //= value.value
    return Value(Value.INTEGER, div_sum)


def println(interpreter, values):
    print(' '.join(map(Value.print_value, values)), file=interpreter.stdout)


def create_list(interpreter, values):
    return Value(Value.LIST, list(values))


def list_map(interpreter, values):
    if not len(values) == 2:
        raise NotEnoughParametersException('map required two params: <function> <list>')
    func, list_value = values
    if func.type != Value.FUNCTION:
        raise UnsupportedParameterType('First parameter of map must be a function')
    if list_value.type != Value.LIST:
        raise UnsupportedParameterType('Second parameter of map must be a list')

    ret = []
    for value in list_value.value:
        ret.append(interpreter.function(func.value, [value], {}))

    return Value(Value.LIST, ret)


def _single_param_list_func(values, name, min_length=False):
    if len(values) == 0:
        raise NotEnoughParametersException('{} requires one parameter: <list>'.format(name))
    if len(values) > 1:
        raise TooManyParametersException('{} requires one parameter: <list>'.format(name))
    l = values[0]
    if l.type != Value.LIST:
        raise UnsupportedParameterType('parameter of {} must be a list'.format(name))
    if min_length and len(l.value) == 0:
        raise UnsupportedParameterType('{}: list needs at least one element'.format(name))
    return l.value


def list_first(interpreter, values):
    l = _single_param_list_func(values, 'first', True)
    return l[0]


def list_last(interpreter, values):
    l = _single_param_list_func(values, 'last', True)
    return l[-1]


def list_head(interpreter, values):
    l = _single_param_list_func(values, 'head')
    return Value(Value.LIST, l[:-1])


def list_tail(interpreter, values):
    l = _single_param_list_func(values, 'tail')
    return Value(Value.LIST, l[1:])


def boolean_not(interpreter, values):
    if len(values) == 0:
        raise NotEnoughParametersException('not requires one parameter')
    if len(values) > 1:
        raise TooManyParametersException('not requires one parameter')
    boolean = values[0]
    if boolean.type != Value.BOOLEAN:
        raise UnsupportedParameterType('parameter of not must be a boolean')
    return Value(Value.BOOLEAN, not boolean.value)


def boolean_and(interpreter, values):
    if len(values) < 2:
        raise NotEnoughParametersException('and requires at least two parameters')
    if values[0].type != Value.BOOLEAN:
        raise UnsupportedParameterType('parameters of and must be booleans')
    boolean = values[0].value
    for value in values[1:]:
        if not value.type == Value.BOOLEAN:
            raise UnsupportedParameterType('parameters of and must be booleans')
        boolean = boolean and value.value
    return Value(Value.BOOLEAN, boolean)


def boolean_or(interpreter, values):
    if len(values) < 2:
        raise NotEnoughParametersException('or requires at least two parameters')
    if values[0].type != Value.BOOLEAN:
        raise UnsupportedParameterType('parameters of or must be booleans')
    boolean = values[0].value
    for value in values[1:]:
        if not value.type == Value.BOOLEAN:
            raise UnsupportedParameterType('parameters of or must be booleans')
        boolean = boolean or value.value
    return Value(Value.BOOLEAN, boolean)


def _two_param_integer_func(values, name):
    if len(values) < 2:
        raise NotEnoughParametersException('{} requires three parameters'.format(name))
    if len(values) > 2:
        raise TooManyParametersException('{} requires three parameters'.format(name))
    if values[0].type != Value.INTEGER:
        raise UnsupportedParameterType('first parameter of {} must be an integer'.format(name))
    if values[1].type != Value.INTEGER:
        raise UnsupportedParameterType('second parameter of {} must be an integer'.format(name))
    return values[0].value, values[1].value


def smaller_than(interpreter, values):
    value1, value2 = _two_param_integer_func(values, '<')
    if value1 < value2:
        return Value(Value.BOOLEAN, True)
    else:
        return Value(Value.BOOLEAN, False)


def bigger_than(interpreter, values):
    value1, value2 = _two_param_integer_func(values, '<')
    if value1 > value2:
        return Value(Value.BOOLEAN, True)
    else:
        return Value(Value.BOOLEAN, False)


def smaller_or_equal_than(interpreter, values):
    value1, value2 = _two_param_integer_func(values, '<')
    if value1 <= value2:
        return Value(Value.BOOLEAN, True)
    else:
        return Value(Value.BOOLEAN, False)


def bigger_or_equal_than(interpreter, values):
    value1, value2 = _two_param_integer_func(values, '<')
    if value1 >= value2:
        return Value(Value.BOOLEAN, True)
    else:
        return Value(Value.BOOLEAN, False)


def equals(interpreter, values):
    if len(values) < 2:
        raise NotEnoughParametersException('== requires two parameters')
    if len(values) > 2:
        raise TooManyParametersException('== requires two parameters')
    value1, value2 = values
    if value1.type != value2.type:
        raise UnsupportedParameterType('both parameters of == must be the same type')
    return value1.value == value2.value


def not_equals(interpreter, values):
    if len(values) < 2:
        raise NotEnoughParametersException('== requires two parameters')
    if len(values) > 2:
        raise TooManyParametersException('== requires two parameters')
    value1, value2 = values
    if value1.type != value2.type:
        raise UnsupportedParameterType('both parameters of == must be the same type')
    return value1.value != value2.value


def if_builtin(interpreter, values):
    if len(values) < 3:
        raise NotEnoughParametersException('if requires three parameters')
    if len(values) > 3:
        raise TooManyParametersException('if requires three parameters')

    condition, true_value, false_value = values

    if condition.type != Value.BOOLEAN:
        raise UnsupportedParameterType('first parameter of if must be a boolean')

    if condition.value:
        return true_value
    else:
        return false_value

builtins = {
    '+': plus,
    '-': minus,
    '*': mul,
    '/': div,

    '<': smaller_than,
    '>': bigger_than,
    '<=': smaller_or_equal_than,
    '>=': bigger_or_equal_than,

    '==': equals,
    '!=': not_equals,

    'println': println,

    'list': create_list,
    'map': list_map,
    'first': list_first,
    'last': list_last,
    'head': list_head,
    'tail': list_tail,

    'not': boolean_not,
    'and': boolean_and,
    'or': boolean_or,

    'if': if_builtin,
}
