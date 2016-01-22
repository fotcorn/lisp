from unittest import TestLoader, TextTestRunner, TestSuite

from lisp.tests.math import MathTestCase

if __name__ == '__main__':
    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase(MathTestCase),
    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
