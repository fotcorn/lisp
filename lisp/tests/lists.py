from lisp.interpreter_exceptions import NotEnoughParametersException, TooManyParametersException, \
    UnsupportedParameterType
from lisp.tests.base_test import BaseTestCase


class ListTestCase(BaseTestCase):

    def test_first(self):
        self.assert_stdout('(println (first (list 1 2 3)))', '1\n')

    def test_first_missing_param(self):
        self.assert_exception('(first)', NotEnoughParametersException)

    def test_first_too_many_params(self):
        self.assert_exception('(first (list 1) (list 2))', TooManyParametersException)

    def test_first_wrong_param_type(self):
        self.assert_exception('(first 1)', UnsupportedParameterType)
