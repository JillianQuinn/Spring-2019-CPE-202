# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *


class test_expressions(unittest.TestCase):
    def test_postfix_eval_01(self):
        """Test two numbers"""
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)
        """Test exponents"""
        self.assertEqual(postfix_eval("5 1 2 + 4 ** + 3 -"), 83)
        self.assertEqual(postfix_eval("6 4 3 + 2 - * 6 /"), 5)
        """Test long expressions"""
        self.assertEqual(postfix_eval("5 2 4 * + 7 2 - 4 6 2 / 2 - * + 4 - +"), 18)
        """Testing Floats."""
        self.assertAlmostEqual(postfix_eval("3.568000 5.98678567 +"), 9.55478567)

    def test_postfix_eval_02(self):
        """Testing invalid input exception"""
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        """Testing too few operands"""
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        """Testing too many operands"""
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_postfix_eval_05(self):
        """Testing float with >>"""
        try:
            postfix_eval("3 3 / 1 >>")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Illegal bit shift operand")

    def test_postfix_eval_06(self):
        """Testing zero division"""
        with self.assertRaises(ValueError):
            postfix_eval("3 0 /")

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("8 + 3 * 4 + ( 6 - 2 + 2 * ( 6 / 3 - 1 ) - 3 )"),
                         "8 3 4 * + 6 2 - 2 6 3 / 1 - * + 3 - +")
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("2 ** 4 ** 5 ** 5 ** 3 ** 5 ** 4"), "2 4 5 5 3 5 4 ** ** ** ** ** **")
        self.assertEqual(infix_to_postfix("2 >> 4 ** 5"), "2 4 >> 5 **")
        self.assertEqual(infix_to_postfix("6"), "6")
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3"), "3 4 2 * 1 5 - 2 3 ** ** / +")
        self.assertEqual(infix_to_postfix("5 * ( 6 + 3 - 7 * 3 + 2 ) / 6"), "5 6 3 + 7 3 * - 2 + * 6 /")

    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"), "3 2 1 / - 4 5 / 6 - *")


if __name__ == "__main__":
    unittest.main()
