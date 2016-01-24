from lisp.tests.base_test import BaseTestCase


class ConditionalTestCase(BaseTestCase):

    def test_smaller_than_true(self):
        self.assert_stdout('(println (< 5 9))', 'true\n')

    def test_smaller_than_false(self):
        self.assert_stdout('(println (< 5 3))', 'false\n')

    def test_bigger_than_true(self):
        self.assert_stdout('(println (> 5 9))', 'false\n')

    def test_bigger_than_false(self):
        self.assert_stdout('(println (> 5 3))', 'true\n')

    # smaller & bigger than or equal
    def test_smaller_than_equal_true(self):
        self.assert_stdout('(println (<= 5 9))', 'true\n')
        self.assert_stdout('(println (<= 5 5))', 'true\n')

    def test_smaller_than_equal_false(self):
        self.assert_stdout('(println (<= 5 3))', 'false\n')

    def test_bigger_than_equal_true(self):
        self.assert_stdout('(println (>= 5 9))', 'false\n')
        self.assert_stdout('(println (>= 5 5))', 'true\n')

    def test_bigger_than_equal_false(self):
        self.assert_stdout('(println (>= 5 3))', 'true\n')
