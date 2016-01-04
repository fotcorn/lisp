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

builtins = {
    '+': plus,
    '-': minus,
    '*': mul,
    '/': div,
    'println': println,
    'list': create_list,
}
