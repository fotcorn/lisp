from lexer import Token


class ValueNode(object):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return u'{}: {}'.format(self.__class__.__name__, self.value)


class Number(ValueNode):
    pass


class String(ValueNode):
    pass


class Identifier(ValueNode):
    pass


class Function(object):
    def __init__(self, param_names, expression):
        self.param_names = param_names
        self.expression = expression

    def __str__(self):
        return u'Function: [{}] ({})'.format(u', '.join(map(unicode, self.param_names)), self.expression)


class Call(object):
    def __init__(self, expressions):
        self.expressions = expressions

    def __str__(self):
        return u'Call: ({})'.format(u', '.join(map(unicode, self.expressions)))


def parse(tokens):
    parser = Parser(tokens)
    return parser.parse()


class Parser(object):

    def __init__(self, tokens):
        self.tokens = tokens
        self.i = 0
        self.current_token = self.tokens[self.i]
        self.last_token = None

    def parse(self):
        expressions = []
        while True:
            if self.current_token.type == Token.END_OF_FILE:
                break
            elif self.accept(Token.EXPRESSION_START):
                expressions.append(self.call())
        return expressions

    def next_token(self):
        self.i += 1
        self.last_token = self.current_token
        self.current_token = self.tokens[self.i]

    def accept(self, token_type):
        if self.current_token.type == token_type:
            self.next_token()
            return True
        elif self.current_token.type == Token.END_OF_FILE:
            raise Exception(u'Unexpected end of file {}'.format(self.current_token))
        return False

    def expect(self, token_type):
        if not self.accept(token_type):
            raise Exception(u'Parse error on token {}'.format(self.current_token))

    def expression(self):
        if self.current_token.type == Token.IDENTIFIER and self.current_token.value == 'fn':
            return self.function()
        else:
            return self.call()

    def value(self):
        if self.accept(Token.NUMBER):
            return Number(self.last_token.value)
        elif self.accept(Token.STRING):
            return String(self.last_token.value)
        elif self.accept(Token.IDENTIFIER):
            return Identifier(self.last_token.value)
        elif self.accept(Token.EXPRESSION_START):
            return self.expression()
        elif self.accept(Token.EXPRESSION_END):
            return None
        else:
            raise Exception(u'Parse error on token {}'.format(self.current_token))

    def call(self):
        current_expression = []
        while True:
            value = self.value()
            if value is None:
                break
            current_expression.append(value)
        return Call(current_expression)

    def function(self):
        self.next_token()
        self.expect(Token.BRACKET_OPEN)
        function_params = []
        while True:
            if self.accept(Token.IDENTIFIER):
                function_params.append(self.last_token.value)
                if self.accept(Token.COMMA):
                    continue
                elif self.accept(Token.BRACKET_CLOSE):
                    break
            elif self.accept(Token.BRACKET_CLOSE):
                break
            else:
                raise Exception(u'Parse error in function parameter list on token {}'.format(self.current_token))
        value = self.value()
        if not value:
            raise Exception(u'Parse error on token {}'.format(self.current_token))
        self.expect(Token.EXPRESSION_END)
        return Function(function_params, value)
