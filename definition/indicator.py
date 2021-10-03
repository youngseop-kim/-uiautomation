
import json

def is_string_expression(expression):
    return isinstance(expression, str)

def is_object_expression(expression):
    return isinstance(expression, dict)

class IndicatorExpression:
    
    def __init__(self, expression):
        if is_string_expression(expression):
            expression = json.loads(expression)

        self.__expression = expression
        self.__private_expression = {}
        self.__public_expression = {}

        for key, value in self.__expression.items():
            if key.startswith('__'):
                self.__private_expression[key] = value

            else:
                self.__public_expression[key] = value

    @property
    def expression(self):
        return self.__expression

    @property
    def private_expression(self):    
        return self.__private_expression

    @property
    def public_expression(self):    
        return self.__public_expression

class Indicator:
    pass