
import json
import re
import fnmatch

def is_string_expression(expression):
    return isinstance(expression, str)

def is_object_expression(expression):
    return isinstance(expression, dict)

class ResolverGuideExpression:
    
    def __init__(self, expression):
        if is_string_expression(expression):
            expression = json.loads(expression)

        else:
            expression = expression

        self.__expression = expression
        self.__private_expression = {}
        self.__public_expression = {}

        for key, value in self.__expression.items():
            if key.startswith('__'):
                self.__private_expression[key] = value

            else:
                self.__public_expression[key] = value

    def __str__(self):
        return str(self.__expression)

    def __repr__(self):
        return repr(self.__expression)

    @property
    def expression(self):
        return self.__expression

    @property
    def private_expression(self):    
        return self.__private_expression

    @property
    def public_expression(self):    
        return self.__public_expression

class ResolverGuide:

    @classmethod
    def is_match_fnmatch(cls, resolver, public_expression):
        conditions = []
        for key, value in public_expression.items():
            property_ = str(resolver.resolve_property(key))
            conditions.append(fnmatch.fnmatch(property_, value))
        return all(conditions)

    @classmethod
    def is_match_regex(cls, resolver, public_expression):
        conditions = []
        for key, value in public_expression.items():
            property_ = str(resolver.resolve_property(key))
            conditions.append(re.match(value, property_))
        return all(conditions)

    @classmethod
    def point_horizontally(cls, resolver, public_expression, private_expression):
        generator = resolver.iterate_on_child_resolvers()
        match_method = getattr(cls, private_expression['__match_method'])

        for child_resolver in generator:
            if match_method(child_resolver, public_expression):
                return child_resolver

            cls.point_horizontally(
                resolver=child_resolver, 
                public_expression=public_expression, 
                private_expression=private_expression
                )

    @classmethod
    def point_vertically(cls, resolver, public_expression, private_expression):
        pass