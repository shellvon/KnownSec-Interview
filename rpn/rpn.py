# encoding=utf8
# author:shellvon

import operator
import string


ARITHMETIC_OPERATORS = {
    '+':  operator.add, '-':  operator.sub,
    '*':  operator.mul, '/':  operator.div,
    '%':  operator.mod, '^': operator.pow,
    '//': operator.floordiv,
}


class BadPostfixNotation(Exception):
    """NotImplemented"""
    def __init__(self, message):
        self._message = "BadPostfixNotation when build:{0}".format(message)

    @property
    def message(self):
        return self._message


def validate_expr(expression):
    """
    Validate the expression
    """
    pass


def torpn(expr):
    """
    A General Infix-to-Postfix Conversion.
    The solution assumes that all expression are the right infix expression.
    See:
        http://interactivepython.org/runestone/static/pythonds/BasicDS/stacks.html
    RPN:
        Postfix Expressions(http://en.wikipedia.org/wiki/Reverse_Polish_notation)
    For example:
        A * B + C * D => A B * C D * +
        ( A + B ) * C - ( D - E ) * ( F + G ) =>A B + C * D E - F G + * -
    TODO:
        check valid of the expr.
    """

    postfixchar = string.letters+string.digits
    precedence = {'^': 3, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    token_list = expr.split()
    postfix_stack, op_stack = [], []
    for token in token_list:
        if token in postfixchar:
            postfix_stack.append(token)
        elif token == '(':
            op_stack.append(token)
        elif token == ')':
            tmp_token = op_stack.pop()
            while tmp_token != '(':
                postfix_stack.append(tmp_token)
                tmp_token = op_stack.pop()
        else:
            while len(op_stack) != 0 and precedence[op_stack[-1]] >= precedence[token]:
                postfix_stack.append(op_stack.pop())
            op_stack.append(token)
    while len(op_stack) != 0:
        postfix_stack.append(op_stack.pop())
    return ' '.join(postfix_stack)


def postfix(expr, operators=ARITHMETIC_OPERATORS):
    """
    Postfix Evaluation
    """
    stack = []

    def func(stack, var):
        stack[-2:] = [var]    # lambda can't use assginments.
    [func(stack, operators[var](*stack[-2:])) if var in operators else stack.append(int(var)) for var in expr.split()]
    return stack.pop()
