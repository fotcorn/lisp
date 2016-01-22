

class BaseInterpreterException(Exception):
    def __init__(self, *args, **kwargs):
        super(BaseInterpreterException, self).__init__(*args, **kwargs)


class NotEnoughParametersException(BaseInterpreterException):
    pass


class TooManyParametersException(BaseInterpreterException):
    pass


class UnsupportedParameterType(BaseInterpreterException):
    pass
