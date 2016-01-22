
class Value(object):
    INTEGER = 1
    STRING = 2
    FUNCTION = 3
    LIST = 4

    def __init__(self, value_type, value, variable_context=None):
        self.type = value_type
        self.value = value
        self.variable_context = variable_context

    def __str__(self):
        if self.type == Value.INTEGER:
            return u'Integer: {}'.format(self.value)
        elif self.type == Value.STRING:
            return u'String: {}'.format(self.value)
        elif self.type == Value.FUNCTION:
            return u'Function: {}'.format(self.value)
        elif self.type == Value.LIST:
            return u'List: [{}]'.format(', '.join(map(unicode, self.value)))

    def __unicode__(self):
        return self.__str__()

    def print_value(self):
        if self.type == Value.INTEGER:
            return unicode(self.value)
        elif self.type == Value.STRING:
            return self.value
        elif self.type == Value.FUNCTION:
            return unicode(self.value)
        elif self.type == Value.LIST:
            return u'[{}]'.format(', '.join(map(Value.print_value, self.value)))
