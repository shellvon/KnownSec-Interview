# encoding=utf8
# author:shellvon

"""
Use unittest module for unit testing
"""


import unittest
from rpn import postfix, torpn


class TestInfixToRPN(unittest.TestCase):
    """
    Simple converts the infix expression to RPN(the postfix)
    """
    def setUp(self):
        # add some test cases
        self.postfix_expr = "5 1 2 + 4 * + 3 -"
        self.infix_expr = "( 5 + 1 ) * 2 - ( 3 - 1 ) * ( 6 + 7 )"
        self.infix_expr_without_brace = "5 + 1 * 3"
        self.infix_expr_with_power = "5 ^ 3 - 3 * 2 + 3"
        # self.infix_expr_illegal = "4 + 3 -"
        self.infix_expr_with_empty = ''
        self.infix_expr_with_single = '12'

    def test_torpn(self):
        self.assertEqual(torpn(self.infix_expr), ' '.join(list("51+2*31-67+*-")))
        self.assertEqual(torpn(self.infix_expr_with_power), '5 3 ^ 3 2 * - 3 +')
        self.assertEqual(torpn(self.infix_expr_without_brace), '5 1 3 * +')
        self.assertEqual(torpn(self.infix_expr_with_empty), '')
        self.assertEqual(torpn(self.infix_expr_with_single), '12')

    def test_evalpostfix(self):
        self.assertEqual(postfix(self.postfix_expr), 14)
        self.assertEqual(postfix(torpn(self.infix_expr)), -14)
        self.assertEqual(postfix(torpn(self.infix_expr_with_power)), 122)
        self.assertEqual(postfix(torpn(self.infix_expr_without_brace)), 8)
        self.assertEqual(postfix(torpn(self.infix_expr_with_single)), 12)

    def test_exception(self):
        pass

    def tearDown(self):
        pass    # the code to do tear down
if __name__ == '__main__':
    unittest.main()
