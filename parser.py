from lexer import Token


class Number(object):
    def __init__(self, value):
        self.value = value


class String(object):
    def __init__(self, value):
        self.value = value


class Identifier(object):
    def __init__(self, value):
        self.value = value


class Function(object):
    def __init__(self, names, expressions):
        self.names = names
        self.expressions = self.expressions


class Expression(object):
    def __init__(self, expressions):
        self.expressions = expressions


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
                expressions.append(self.expression())
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
        current_expression = []
        while True:
            if self.accept(Token.NUMBER):
                current_expression.append(Number(self.last_token.value))
            elif self.accept(Token.STRING):
                current_expression.append(String(self.last_token.value))
            elif self.accept(Token.IDENTIFIER):
                current_expression.append(Identifier(self.last_token.value))
            elif self.accept(Token.EXPRESSION_END):
                break
            else:
                raise Exception(u'Parse error on token {}'.format(self.current_token))
        return Expression(current_expression)
