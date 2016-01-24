from unittest import TestLoader, TextTestRunner, TestSuite

from lisp.tests.boolean import BooleanTestCase
from lisp.tests.conditionals import ConditionalTestCase
from lisp.tests.lists import ListTestCase
from lisp.tests.math import MathTestCase

if __name__ == '__main__':
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(BooleanTestCase),
        loader.loadTestsFromTestCase(ConditionalTestCase),
        loader.loadTestsFromTestCase(ListTestCase),
        loader.loadTestsFromTestCase(MathTestCase),
    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
