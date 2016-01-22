from unittest import TestLoader, TextTestRunner, TestSuite

from lisp.tests.boolean import BooleanTestCase
from lisp.tests.lists import ListTestCase
from lisp.tests.math import MathTestCase

if __name__ == '__main__':
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(MathTestCase),
        loader.loadTestsFromTestCase(ListTestCase),
        loader.loadTestsFromTestCase(BooleanTestCase),
    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
