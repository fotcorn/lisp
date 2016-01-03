
class Value(object):
    INTEGER = 1
    STRING = 2
    FUNCTION = 3

    def __init__(self, value_type, value):
        self.type = value_type
        self.value = value
