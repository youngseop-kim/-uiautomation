
import re
import fnmatch

class ObjectResolverPointerExpression:
    '''
    expressions (start)             ->  [
        - expression 1st (instance)           {'property_key' : 'property_value'},
        - expression 2nd (instance)           {'property_key' : 'property_value'},
        - ...                                 ...,
        - expression nth (instance)           {'property_key' : 'property_value'}
    expressions (end)                   ]
    '''
    
    def __init__(self, expression):
        self.__expression = expression
        self.__public_expression = {}
        self.__private_expression = {}

        for key, value in self.__expression.items():
            if key.startswith('__'):
                self.__private_expression[key] = value
            
            else:
                self.__public_expression[key] = value
        
    def __getitem__(self, key):
        return self.__expression[key]

    def __str__(self):
        return str(self.__expression)

    def __repr__(self):
        return repr(self.__expression)

    def expression(self):
        return self.__expression

    def public_expression(self):
        return self.__public_expression

    def private_expression(self):
        return self.__private_expression

    def keys(self):
        return self.__expression.keys()

    def values(self):
        return self.__expression.values()

    def items(self):
        return self.__expression.items()

class ObjectResolverPointer:
    tree_walker = None

    @classmethod
    def call(cls, func, *args, **kwargs):
        return func(*args, **kwargs)

    @classmethod
    def callback_is_match_fnmatch(
        cls, 
        object_resolver, 
        public_expression
        ):

        condition_collection = []
        for key, value in public_expression.items():
            property = str(object_resolver.resolve_property(key))
            condition = fnmatch.fnmatch(property, value)
            condition_collection.append(condition)
        return all(condition_collection)

    @classmethod
    def callback_is_match_regex(
        cls, 
        object_resolver, 
        public_expression
        ):

        condition_collection = []
        for key, value in public_expression.items():
            property = str(object_resolver.resolve_property(key))
            condition = re.match(value, property)
            condition_collection.append(condition)
        return all(condition_collection)
    
    @classmethod
    def callback_point_vertically(
        cls,
        object_resolver_collection, 
        object_resolver,
        public_expression,
        private_expression
        ):

        generator = object_resolver.iterate_on_children(cls.tree_walker)
        match_method = getattr(cls, private_expression['__match_method'])
        
        for index, child_object_resolver in enumerate(generator):
            if match_method(child_object_resolver, public_expression):
                result_collection.append(child_object_resolver)

            if len(result_collection) > 0:
                break

            cls.call(
                cls.callback_point_vertically,
                result_collection,
                [child_object_resolver], 
                public_expression,
                private_expression
                )

    @classmethod
    def callback_point_horizontally(
        cls, 
        object_resolver_collection, 
        object_resolver,
        public_expression,
        private_expression
        ):

        generator = object_resolver.iterate_on_children(cls.tree_walker)
        match_method = getattr(cls, private_expression['__match_method'])
        
        for index, child_object_resolver in enumerate(generator):
            if match_method(child_object_resolver, public_expression):
                object_resolver_collection.append(child_object_resolver)

            if len(object_resolver_collection) > 0:
                break


    @classmethod
    def point(cls, object_resolver, expressions):
        expression_collection = []
        for expression in expressions:
            expression = ObjectResolverPointerExpression(expression)
            expression_collection.append(expression)

        index = 0
        while index < len(expression_collection):
            object_resolver_collection = []
            expression = expression_collection[index]
            public_expression = expression.public_expression()
            private_expression = expression.private_expression()
            
            cls.call(
                cls.callback_points,
                object_resolver_collection,
                object_resolver, 
                public_expression, 
                private_expression
                )
            
            object_resolver = object_resolver_collection[0]
            index+=1
        
        return object_resolver

if __name__ == '__main__':
    # temp
    from base import UIAutomation
    from object_resolver import *
    from object_resolver_reference import *

    ObjectResolver.reference_for_class = ObjectResolverReferenceForClass()
    ObjectResolver.reference_for_pattern = ObjectResolverReferenceForPattern()
    ObjectResolver.reference_for_property = ObjectResolverReferenceForProperty()
    ObjectResolverPointer.tree_walker = UIAutomation.RawViewWalker

    import datetime
    object_resolver_ = ObjectResolver.__subclass_from__(UIAutomation.GetRootElement())
    start = datetime.datetime.now()
    object_resolver = ObjectResolverPointer.call(
        ObjectResolverPointer.callback_point,
        object_resolver_,
        [
            {'name' : '제목 없음 - Windows 메모장', '__match_method' : 'callback_is_match_fnmatch', '__point_method' : ''},
            {'name' : '서식(*)', '__match_method' : 'callback_is_match_fnmatch', '__point_method' : ''},
        ]
        )
    
    print(datetime.datetime.now() - start)
    print(object_resolver )
    