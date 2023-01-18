import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility, number
from measures import *


class TestAll(unittest.TestCase):
    @weight(2)
    @visibility("visible")
    @number("2")
    def testWadlowHeight(self):
        val = feet_to_meters(8.9)
        self.assertEqual(val, 2.71)
        print('End of testing for feet_to_meters for 8.9 feet')

    @weight(2)
    @visibility("visible")
    @number("3")
    def testInchRoundingA(self):
        val = feet_to_inches(3.3)
        self.assertEqual(val, 40)
        print('End of testing for feet_to_inches for 3.3 feet')

    @weight(2)
    @visibility("visible")
    @number("4")
    def testInchRoundingB(self):
        val = feet_to_inches(3.4)
        self.assertEqual(val, 41)
        print('End of testing for feet_to_inches for 3.3 feet')

    @weight(2)
    @visibility("visible")
    @number("5")
    def testMeterRounding(self):
        val = feet_to_meters(52)
        self.assertEqual(val, 15.85)
        print('End of testing for feet_to_meters for 8.9 feet')

