
class Value(object):
    INTEGER = 1
    STRING = 2
    FUNCTION = 3

    def __init__(self, value_type, value):
        self.type = value_type
        self.value = value

    def __str__(self):
        if self.type == Value.INTEGER:
            return u'Integer: {}'.format(self.value)
        elif self.type == Value.INTEGER:
            return u'String: {}'.format(self.value)
        if self.type == Value.FUNCTION:
            return u'Function: {}'.format(self.value)
