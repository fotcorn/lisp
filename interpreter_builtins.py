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


def println(interpreter, values):
    print u' '.join(map(lambda v: unicode(v.value), values))


builtins = {
    '+': plus,
    '-': minus,
    'println': println,
}
