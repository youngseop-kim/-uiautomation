
from re import match
from fnmatch import fnmatch
from json import loads
from sys import setrecursionlimit

from typing import TypeVar, Dict

def is_string_expression(expression):
    return isinstance(expression, str)

def is_object_expression(expression):
    return isinstance(expression, dict)

class ResolverGuideExpression:
    '''
    '''

    def __init__(self, expression):
        if is_string_expression(expression):
            expression = loads(expression)

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
    '''
    '''

    KEY_RESOLVE_METHOD      = '__resolve_method'
    KEY_MATCH_METHOD        = '__match_method'
    KEY_MAX_DEPTH           = '__max_depth'
    KEY_MAX_RECURSION_DEPTH = '__max_recursion_depth'

    @classmethod
    def is_match_fnmatch(
            cls, 
            resolver : TypeVar('(Inherited)Resolver'), 
            resolve_method : str,
            public_expression : Dict[str, str],
            ):
        '''
        '''

        conditions = []

        for key, value in public_expression.items():
            resolve_method = getattr(resolver, resolve_method)
            property_ = str(resolve_method(key))
            conditions.append(fnmatch(property_, value))

        return all(conditions)

    @classmethod
    def is_match_regex(
            cls, 
            resolver : TypeVar('(Inherited)Resolver'), 
            resolve_method : str,
            public_expression : Dict[str, str],
            ):
        '''
        '''

        conditions = []

        for key, value in public_expression.items():
            resolve_method = getattr(resolver, resolve_method)
            property_ = str(resolve_method(key))
            conditions.append(match(value, property_))

        return all(conditions)

    @classmethod
    def iterate_with_breadth_first_search(
            cls,
            resolver : TypeVar('(Inherited)Resolver'), 
            public_expression : Dict[str, str],
            private_expression : Dict[str, str]
            ):
        '''
        '''

        def _procedure(_depth):
            '''
            variable "containers" from upper local context
            variable "resolve_method" from upper local context
            variable "match_method" from upper local context
            variable "max_depth" from upper local context
            '''

            # stop iteration if containers are all empty
            if is_all_empty(containers):
                raise StopIteration()

            # stop iteration when exceed max depth
            if max_depth >= 0 and _depth > max_depth:
                raise StopIteration()

            _container = pick_not_empty(containers)
            _container_next = pick_empty(containers)

            while len(_container) > 0:
                _resolver = _container.pop(0)

                if match_method(_resolver, resolve_method, public_expression):
                    yield _resolver

                for _child_resolver in _resolver.iterate_on_child_resolvers():
                    _container_next.append(_child_resolver)
            
            yield from _procedure(_depth+1)

        # set container
        containers = [[resolver], []]

        # set lambda 'pick_empty'
        pick_empty = \
            lambda x : [i for i in x if len(i) == 0][0]

        # set lambda 'pick_not_empty'
        pick_not_empty = \
            lambda x : [i for i in x if len(i) != 0][0]

        # set lambda 'is_all_empty'
        is_all_empty = \
            lambda x : all([len(i)==0 for i in x])

        # set max depth 
        max_depth = private_expression[cls.KEY_MAX_DEPTH]

        # set max recursion depth
        max_recursion_depth = private_expression[cls.KEY_MAX_RECURSION_DEPTH]

        # set resolve method
        resolve_method = private_expression[cls.KEY_RESOLVE_METHOD]

        # set match method  
        match_method = getattr(cls, private_expression[cls.KEY_MATCH_METHOD])
        
        # set max recursion depth
        setrecursionlimit(max_recursion_depth)

        # yield from procedure
        for resolver_from_procedure in _procedure(0):
            yield resolver_from_procedure

    @classmethod
    def iterate_with_depth_first_search(
            cls,
            resolver : TypeVar('(Inherited)Resolver'), 
            public_expression : Dict[str, str],
            private_expression : Dict[str, str]
            ):
        '''
        '''

        def _procedure(_resolver, _depth):
            '''
            variable "resolve_method" from upper local context
            variable "match_method" from upper local context
            variable "max_depth" from upper local context
            '''

            if match_method(_resolver, resolve_method, public_expression):
                yield _resolver

            for _child_resolver in _resolver.iterate_on_child_resolvers():
                if max_depth >= 0 and _depth > max_depth:
                    raise StopIteration()

                yield from _procedure(_child_resolver, _depth+1)
        
        # set max depth 
        max_depth = private_expression[cls.KEY_MAX_DEPTH]

        # set max recursion depth
        max_recursion_depth = private_expression[cls.KEY_MAX_RECURSION_DEPTH]

        # set resolve method
        resolve_method = private_expression[cls.KEY_RESOLVE_METHOD]

        # set match method  
        match_method = getattr(cls, private_expression[cls.KEY_MATCH_METHOD])

        # set max recursion depth
        setrecursionlimit(max_recursion_depth)

        # yield from procedure
        for resolver_from_procedure in _procedure(resolver, 0):
            yield resolver_from_procedure
