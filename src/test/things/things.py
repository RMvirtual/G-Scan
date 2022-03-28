import unittest

import src.test.things.date as datetest
import src.test.things.user as usertest

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(datetest.TestDate))
    test_suite.addTest(unittest.makeSuite(usertest.TestUser))

    return test_suite

if __name__ == '__main__':
    mySuit=suite()

    runner=unittest.TextTestRunner()
    runner.run(mySuit)