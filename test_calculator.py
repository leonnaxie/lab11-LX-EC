# https://github.com/leonnaxie/lab11-LX-EC
# Partner 1: Leonna Xie
# Partner 2: Emily Chen

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
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(5, 5), 25)
        self.assertEqual(mul(1, 1), 1)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(10, 5), 2)
        self.assertEqual(div(100, 10), 10)
        self.assertEqual(div(4, 2), 2)


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
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(0, 5)
        with self.assertRaises(ValueError):
            log(-1, 5)

        with self.assertRaises(ValueError):
            log(5, 0)
        with self.assertRaises(ValueError):
            log(5, -2)
        with self.assertRaises(ValueError):
            log(5, 1)


    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5.0)
        self.assertEqual(hypotenuse(0, 0), 0.0)
        self.assertEqual(hypotenuse(9, 12), 15)

        self.assertAlmostEqual(hypotenuse(1.5, 2.0), math.hypot(1.5, 2.0), places=6)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-4)

        self.assertEqual(square_root(9), 3.0)
        self.assertEqual(square_root(25), 5.0)
        self.assertAlmostEqual(square_root(2), math.sqrt(2), places=6)
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()