from lisp.tests.base_test import BaseTestCase
from lisp.tests.interpreter_exceptions import NotEnoughParametersException


class MathTestCase(BaseTestCase):

    def test_plus(self):
        self.assert_stdout('(println (+ 1 2 3))', '6\n')

    def test_minus(self):
        self.assert_stdout('(println (- 6 3 2))', '1\n')

    def test_div(self):
        self.assert_stdout('(println (/ 20 2 5))', '2\n')

    def test_mul(self):
        self.assert_stdout('(println (* 2 3 4))', '24\n')

    # single params
    def test_plus_single(self):
        self.assert_stdout('(println (+ 5))', '5\n')

    def test_minus_single(self):
        self.assert_stdout('(println (- 5))', '-5\n')

    def test_div_single(self):
        self.assert_stdout('(println (/ 5))', '5\n')

    def test_mul_single(self):
        self.assert_stdout('(println (* 5))', '5\n')

    # no params
    def test_plus_no_params(self):
        self.assert_exception('(+)', NotEnoughParametersException)

    def test_minus_no_params(self):
        self.assert_exception('(-)', NotEnoughParametersException)

    def test_div_no_params(self):
        self.assert_exception('(/)', NotEnoughParametersException)

    def test_mul_no_params(self):
        self.assert_exception('(*)', NotEnoughParametersException)
