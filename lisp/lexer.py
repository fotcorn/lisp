import re


class Token(object):
    EXPRESSION_START = 1
    EXPRESSION_END = 2
    IDENTIFIER = 3
    NUMBER = 4
    STRING = 5
    BRACKET_OPEN = 6
    BRACKET_CLOSE = 7
    COMMA = 8
    END_OF_FILE = 9

    def __init__(self, token_type, value=None):
        self.type = token_type
        self.value = value

    def __unicode__(self):
        type_name = self.type
        for k, v in self.__class__.__dict__.items():
            if not k.startswith('_') and v == self.type:
                type_name = k
                break
        return u'Token({}, {})'.format(type_name, self.value)

    def __str__(self):
        return unicode(self).encode('utf-8')


def lex(code):
    tokens = []

    i = 0
    while i < len(code):
        char = code[i]
        if char == '(':
            tokens.append(Token(Token.EXPRESSION_START))
        elif char == ')':
            tokens.append(Token(Token.EXPRESSION_END))
        elif char == '[':
            tokens.append(Token(Token.BRACKET_OPEN))
        elif char == ']':
            tokens.append(Token(Token.BRACKET_CLOSE))
        elif char == ',':
            tokens.append(Token(Token.COMMA))
        elif char == '"':
            string = ''
            while True:
                i += 1
                if code[i] == '"':
                    break
                string += code[i]
            tokens.append(Token(Token.STRING, string))
        elif char == '#':
            while True:
                i += 1
                if i >= len(code) or code[i] == '\n':
                    break
        elif re.match(r'[a-zA-Z\+\-\*/<>]', char):
            identifier = char
            while re.match(r'[a-zA-Z\+\-\*/<>0-9]', code[i + 1]):
                identifier += code[i + 1]
                i += 1
            tokens.append(Token(Token.IDENTIFIER, identifier))
        elif re.match(r'[0-9]', char):
            number = char
            while re.match(r'[0-9]', code[i + 1]):
                number += code[i + 1]
                i += 1
            tokens.append(Token(Token.NUMBER, int(number)))
        elif re.match(r'\s', char):  # whitespaces
            pass
        else:
            raise Exception(u'Unknown character: {}'.format(char))

        i += 1
    tokens.append(Token(Token.END_OF_FILE))
    return tokens
