from __future__ import print_function

from lisp.interpreter_value import Value


def plus(interpreter, values):
    plus_sum = 0
    for value in values:
        if not value.type == Value.INTEGER:
            raise Exception('Plus operator: unsupported operand: {}'.format(value))
        plus_sum += value.value
    return Value(Value.INTEGER, plus_sum)


def minus(interpreter, values):
    minus_sum = values[0].value
    for value in values[1:]:
        if not value.type == Value.INTEGER:
            raise Exception('Minus operator: unsupported operand: {}'.format(value))
        minus_sum -= value.value
    return Value(Value.INTEGER, minus_sum)


def mul(interpreter, values):
    mul_sum = values[0].value
    for value in values[1:]:
        if not value.type == Value.INTEGER:
            raise Exception('Minus operator: unsupported operand: {}'.format(value))
        mul_sum *= value.value
    return Value(Value.INTEGER, mul_sum)


def div(interpreter, values):
    div_sum = values[0].value
    for value in values[1:]:
        if not value.type == Value.INTEGER:
            raise Exception('Minus operator: unsupported operand: {}'.format(value))
        div_sum /= value.value
    return Value(Value.INTEGER, div_sum)


def println(interpreter, values):
    print(u' '.join(map(Value.print_value, values)), file=interpreter.stdout)


def create_list(interpreter, values):
    return Value(Value.LIST, list(values))


def list_map(interpreter, values):
    if not len(values) == 2:
        raise Exception(u'map required two params: <function> <list>')
    func, list_value = values
    if func.type != Value.FUNCTION:
        raise Exception(u'First parameter of map must be a function')
    if list_value.type != Value.LIST:
        raise Exception(u'Second parameter of map must be a list')

    ret = []
    for value in list_value.value:
        ret.append(interpreter.function(func.value, [value], {}))

    return Value(Value.LIST, ret)


def _single_param_list_func(values, name, min_length=False):
    if len(values) != 1:
        raise Exception(u'{} required one parameter: <list>'.format(name))
    l = values[0]
    if l.type != Value.LIST:
        raise Exception(u'parameter of {} must be a list'.format(name))
    if min_length and len(l.value) == 0:
        raise Exception(u'{}: list needs at least one element'.format(name))
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
