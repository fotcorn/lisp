
class Value(object):
    INTEGER = 1
    STRING = 2
    FUNCTION = 3
    LIST = 4
    BOOLEAN = 5

    def __init__(self, value_type, value, variable_context=None):
        self.type = value_type
        self.value = value
        self.variable_context = variable_context

    def __str__(self):
        if self.type == Value.INTEGER:
            return 'Integer: {}'.format(self.value)
        elif self.type == Value.STRING:
            return 'String: {}'.format(self.value)
        elif self.type == Value.BOOLEAN:
            return 'Boolean: {}'.format(str(self.value).lower())
        elif self.type == Value.FUNCTION:
            return 'Function: {}'.format(self.value)
        elif self.type == Value.LIST:
            return 'List: [{}]'.format(', '.join(map(str, self.value)))

    def print_value(self):
        if self.type == Value.INTEGER:
            return str(self.value)
        elif self.type == Value.STRING:
            return self.value
        elif self.type == Value.BOOLEAN:
            return str(self.value).lower()
        elif self.type == Value.FUNCTION:
            return str(self.value)
        elif self.type == Value.LIST:
            return '[{}]'.format(', '.join(map(Value.print_value, self.value)))
