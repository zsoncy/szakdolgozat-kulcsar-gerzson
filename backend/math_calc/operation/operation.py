
"""
This module is responsible for solving simple sequences of operations.
"""
class Operation:

    def __init__(self, operation):
        self.operation = operation

    """
    This module evaluates the expression using the eval() built-in Python function. 
    """
    def solve(self):
        return eval(self.operation)
