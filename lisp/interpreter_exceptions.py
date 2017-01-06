

class InterpreterException(Exception):
    def __init__(self, *args, **kwargs):
        super(InterpreterException, self).__init__(*args, **kwargs)


class NotEnoughParametersException(InterpreterException):
    pass


class TooManyParametersException(InterpreterException):
    pass


class UnsupportedParameterType(InterpreterException):
    pass
