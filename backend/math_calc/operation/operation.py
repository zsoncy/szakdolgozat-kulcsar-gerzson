
"""
This module is responsible for solving simple sequences of operations.
"""

def iscorrectoperation(x):
    try:
        eval(x)
        return True
    except (SyntaxError, NameError, ValueError, TypeError):
        return False

class Operation:

    def __init__(self, operation):
        self.operation = operation

    """
    This module evaluates the expression using the eval() built-in Python function. 
    """
    def solve(self):
        return eval(self.operation)
