from lisp.tests.base_test import BaseTestCase


class MathTestCase(BaseTestCase):

    def test_plus(self):
        self.assert_stdout('(println (+ 1 2 3))', '6\n')
