from function_coverage_test_duplicate_code import *

import unittest


def my_suite():
    theSuite = unittest.TestSuite()
    theSuite.addTest(unittest.makeSuite(FunctionCoverageTestDuplicationCode))

    return theSuite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = my_suite()
    runner.run(test_suite)
