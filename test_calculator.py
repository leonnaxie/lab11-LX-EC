import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self): #
        self.assertEqual(add(2,2),4)
        self.assertEqual(add(5,3),8)
        self.assertEqual(add(10,5),15)

    def test_subtract(self):
        self.assertEqual(sub(20,3),17)
        self.assertEqual(sub(6,3),3)
        self.assertEqual(sub(9,9),0)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0,5)
            div(0,9)
            div(0,39)

    def test_logarithm(self):
        self.assertEqual(log(10,100),2)
        self.assertEqual(log(3,81),4)
        self.assertEqual(log(2,64),6)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(3, 1)
            log(4, 0)

    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()