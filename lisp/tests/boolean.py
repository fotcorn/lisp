from lisp.tests.base_test import BaseTestCase


class BooleanTestCase(BaseTestCase):

    def test_true(self):
        self.assert_stdout('(println true)', 'true\n')

    def test_false(self):
        self.assert_stdout('(println false)', 'false\n')

    # not
    def test_not_true(self):
        self.assert_stdout('(println (not true))', 'false\n')

    def test_not_false(self):
        self.assert_stdout('(println (not false))', 'true\n')

    # and
    def test_and_true_true(self):
        self.assert_stdout('(println (and true true))', 'true\n')

    def test_and_true_false(self):
        self.assert_stdout('(println (and true false))', 'false\n')

    def test_and_false_true(self):
        self.assert_stdout('(println (and false true))', 'false\n')

    def test_and_false_false(self):
        self.assert_stdout('(println (and false false))', 'false\n')

    def test_and_triple(self):
        for a in (True, False):
            for b in (True, False):
                for c in (True, False):
                    program = '(println (and {} {} {}))'.format(str(a).lower(), str(b).lower(),
                                                                str(c).lower())
                    stdout = str((a and b) and c).lower() + '\n'
                    self.assert_stdout(program, stdout)

    # or
    def test_or_true_true(self):
        self.assert_stdout('(println (or true true))', 'true\n')

    def test_or_true_false(self):
        self.assert_stdout('(println (or true false))', 'true\n')

    def test_or_false_true(self):
        self.assert_stdout('(println (or false true))', 'true\n')

    def test_or_false_false(self):
        self.assert_stdout('(println (or false false))', 'false\n')

    def test_or_triple(self):
        for a in (True, False):
            for b in (True, False):
                for c in (True, False):
                    program = '(println (or {} {} {}))'.format(str(a).lower(), str(b).lower(),
                                                               str(c).lower())
                    stdout = str((a or b) or c).lower() + '\n'
                    self.assert_stdout(program, stdout)
