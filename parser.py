

class Number(object):
    def __init__(self, value):
        self.value = value


class String(object):
    def __init__(self, value):
        self.value = value


class Identifier(object):
    def __init__(self, value):
        self.value = value


class ParameterNames(object):
    def __init__(self, names):
        self.names = names


def parse(tokens):
    for t in tokens:
        print t
