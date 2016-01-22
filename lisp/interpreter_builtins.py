from __future__ import print_function

from lisp.interpreter_exceptions import NotEnoughParametersException, UnsupportedParameterType, \
    TooManyParametersException
from lisp.interpreter_value import Value


def plus(interpreter, values):
    if len(values) == 0:
        raise NotEnoughParametersException(u'+ requires at least one parameter')
    plus_sum = 0
    for value in values:
        if not value.type == Value.INTEGER:
            raise UnsupportedParameterType(u'+ operator: unsupported operand: {}'.format(value))
        plus_sum += value.value
    return Value(Value.INTEGER, plus_sum)


def minus(interpreter, values):
    if len(values) == 0:
        raise NotEnoughParametersException(u'- requires at least one parameter')
    minus_sum = values[0].value
    if len(values) == 1:
        minus_sum = - minus_sum
    else:
        for value in values[1:]:
            if not value.type == Value.INTEGER:
                raise UnsupportedParameterType(u'- operator: unsupported operand: {}'.format(value))
            minus_sum -= value.value
    return Value(Value.INTEGER, minus_sum)


def mul(interpreter, values):
    if len(values) == 0:
        raise NotEnoughParametersException(u'* requires at least one parameter')
    mul_sum = values[0].value
    for value in values[1:]:
        if not value.type == Value.INTEGER:
            raise UnsupportedParameterType(u'* operator: unsupported operand: {}'.format(value))
        mul_sum *= value.value
    return Value(Value.INTEGER, mul_sum)


def div(interpreter, values):
    if len(values) == 0:
        raise NotEnoughParametersException(u'/ requires at least one parameter')
    div_sum = values[0].value
    for value in values[1:]:
        if not value.type == Value.INTEGER:
            raise UnsupportedParameterType(u'/ operator: unsupported operand: {}'.format(value))
        div_sum /= value.value
    return Value(Value.INTEGER, div_sum)


def println(interpreter, values):
    print(u' '.join(map(Value.print_value, values)), file=interpreter.stdout)


def create_list(interpreter, values):
    return Value(Value.LIST, list(values))


def list_map(interpreter, values):
    if not len(values) == 2:
        raise NotEnoughParametersException(u'map required two params: <function> <list>')
    func, list_value = values
    if func.type != Value.FUNCTION:
        raise UnsupportedParameterType(u'First parameter of map must be a function')
    if list_value.type != Value.LIST:
        raise UnsupportedParameterType(u'Second parameter of map must be a list')

    ret = []
    for value in list_value.value:
        ret.append(interpreter.function(func.value, [value], {}))

    return Value(Value.LIST, ret)


def _single_param_list_func(values, name, min_length=False):
    if len(values) == 0:
        raise NotEnoughParametersException(u'{} requires one parameter: <list>'.format(name))
    if len(values) > 0:
        raise TooManyParametersException(u'{} requires one parameter: <list>'.format(name))
    l = values[0]
    if l.type != Value.LIST:
        raise UnsupportedParameterType(u'parameter of {} must be a list'.format(name))
    if min_length and len(l.value) == 0:
        raise UnsupportedParameterType(u'{}: list needs at least one element'.format(name))
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

builtins = {
    '+': plus,
    '-': minus,
    '*': mul,
    '/': div,
    'println': println,
    'list': create_list,
    'map': list_map,
    'first': list_first,
    'last': list_last,
    'head': list_head,
    'tail': list_tail,
}
