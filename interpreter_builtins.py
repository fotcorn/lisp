from interpreter_value import Value


def plus(interpreter, values):
    plus_sum = 0
    for value in values:
        if not value.type == Value.INTEGER:
            raise Exception('Plus operator: unsupported operand: {}'.format(value))
        plus_sum += value.value
    return Value(Value.INTEGER, plus_sum)


def minus(interpreter, values):
    minus_sum = 0
    for value in values:
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
    print u' '.join(map(Value.print_value, values))


def create_list(interpreter, values):
    return Value(Value.LIST, list(values))


def map_list(interpreter, values):
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


builtins = {
    '+': plus,
    '-': minus,
    '*': mul,
    '/': div,
    'println': println,
    'list': create_list,
    'map': map_list,
}
