import unittest

import src.test.things.date as datetest
import src.test.things.user as usertest

class ThingsTestSuite(unittest.TestSuite):

    def __init__(self) -> None:
        super().__init__(datetest.TestDate(), usertest.TestUser())

if __name__ == '__main__':
    unittest.main()