
from definition.base import dumps_comobject
from definition.base import loads_comobject
from definition.base import is_null_pointer

from definition.base import UIAutomationClient
from definition.base import UIAutomationUnknownType
from definition.base import UIAutomationElementType
from definition.base import UIAutomationElementArrayType

class MustInheritError(Exception):
    
    def __init__(self, instance):
        subclasses = instance.__class__.__subclasses__()
        super().__init__(f'this class must inherit from {subclasses}')

class NotSupportedTypeError(Exception):

    def __init__(self, type_):
        super().__init__(f'this class supports only {type_}')

class NotIdentifiedKey(Exception):

    def __init__(self, key):
        self._key = key

    def __str__(self):
        return f'[not identified "{self._key}"]'

    def __repr__(self):
        return f'[not identified "{self._key}"]'

class NotSupportedKey(Exception):

    def __init__(self, key):
        self._key = key

    def __str__(self):
        return f'[not supported "{self._key}"]'

    def __repr__(self):
        return f'[not supported "{self._key}"]'

def is_unknown_type(automation_object):
    '''
    is comtypes pointer from unknown interface
    '''
    return isinstance(automation_object, UIAutomationUnknownType)
    
def is_automation_element_type(automation_object):
    '''
    is comtypes pointer from autiomation element interface
    '''
    return isinstance(automation_object, UIAutomationElementType)

def is_automation_element_array_type(automation_object):
    '''
    is comtypes pointer from autiomation element array interface
    '''
    return isinstance(automation_object, UIAutomationElementArrayType)

def raise_exception_unless_inherit(method):
    '''
    * this is decorator method
    raise exception
    if try to create instance directly with primary class
    '''
    def decorated(self, *args, **kwargs):
        if self.__class__.__bases__[0] == object:
            raise MustInheritError(self)

        return method(self, *args, **kwargs)
    return decorated

def raise_exception_unless_automation_element_type(method):
    '''
    * this is decorator method
    raise exception
    if instance's variable "automation_object" is not automation element type
    '''
    def decorated(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        if not is_automation_element_type(self._automation_object):
            raise NotSupportedTypeError(UIAutomationElementType)

        return result
    return decorated

class ResolverFactory(object):
    '''
    create instance from inherited resolver class with argument "automation_object"
    according to resolver factory strategy named class variable "_strategy"
    and also your resolver class could be supported by updating resolver factory strategy  
    
    * resolver factory strategy consists of 
        - key : type check method name
        - value : create instance method name
        - both method objects could be append by calling method "append_strategy"
    '''

    _strategy = {
        'is_automation_element_type' : 'create_instance_from_automation_element',
        'is_automation_element_array_type' : 'create_instances_from_automation_element_array'
        }

    def __new__(cls, automation_object):
        return cls.create_instance(automation_object)

    @classmethod
    def create_instance(cls, automation_object):
        '''
        return resolver instance that is satisfied resolver factory strategy
        '''
        for key, value in cls._strategy.items():
            type_method = getattr(cls, key)
            create_method = getattr(cls, value)

            if type_method(automation_object):
                return create_method(automation_object)

        raise NotSupportedTypeError()

    @classmethod
    def create_instance_from_root(cls):
        '''
        return root resolver instance that is satisfied resolver factory strategy
        '''
        return cls.__new__(cls, UIAutomationClient.GetRootElement())

    @classmethod
    def append_strategy(cls, type_method, create_method):
        '''
        * this method is for appending resolver factory strategy

        type method (key) should be designed as below,
            - arguments receive an "automation object"
            - return as boolean 

        create method (value) should be designed as below,
            - arguments receive an "automation object"
            - return as any object
        '''
        setattr(cls, type_method.__name__, type_method)
        setattr(cls, create_method.__name__, create_method)
        cls._strategy[type_method.__name__] = create_method.__name__
        return True

    @classmethod
    def is_automation_element_type(cls, automation_object):
        '''
        * this method is for resolver factory strategy key (type)
        '''
        return is_automation_element_type(automation_object)

    @classmethod
    def is_automation_element_array_type(cls, automation_object):
        '''
        * this method is for resolver factory strategy key (type)
        '''
        return is_automation_element_array_type(automation_object)

    @classmethod
    def create_instance_from_automation_element(cls, automation_object):
        '''
        * this method is for resolver factory strategy value (create)
        '''
        return AutomationElementResolver(automation_object)

    @classmethod
    def create_instances_from_automation_element_array(cls, automation_object):
        '''
        * this method is for resolver factory strategy value (create)
        '''
        array = tuple()
        for index in range(automation_object.Length):
            array+=(AutomationElementResolver(automation_object.GetElement(index)),)

        return array  

class Resolver(object):
    '''
    resovler class is designed to provide easy-handle of automation element
    '''

    _tree_walker = UIAutomationClient.RawViewWalker
    _automation_object = None

    _reference_properties = None
    _reference_patterns = None

    @raise_exception_unless_inherit
    def __init__(self, automation_object):
        self._automation_object = automation_object

    @raise_exception_unless_inherit
    def _ready_for_pickle_dumps(self):
        '''
        '''
        self._automation_object = dumps_comobject(
            object_ = self._automation_object
            )
    
    @raise_exception_unless_inherit
    def _ready_for_pickle_loads(self):
        '''
        '''
        self._automation_object = loads_comobject(
            comtype = UIAutomationElementType, 
            bytes_ = self._automation_object
            )

class AutomationElementResolver(Resolver):
    '''
    automation element resolver hierarchy
    - root automation element resolver
        - parent automation element resolver         | siblings ...
            - self automation element resolver       | sibling automation element resolver
                - child automation element resolver  | siblings ...
    '''

    @raise_exception_unless_automation_element_type
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return str(self.__class__.__name__)

    def __repr__(self):
        return repr(self.__class__.__name__)

    def _resolve_property(self, key):
        '''
        return resolved automation element property
        '''
        id_ = getattr(self._reference_properties, key)
        property_ = self._automation_object.GetCurrentPropertyValue(id_)
        return property_
        
    def _resolve_pattern(self, key):
        '''
        return resolved automation element pattern
        '''
        id_, interface = getattr(self._reference_patterns, key)
        pattern_ = self._automation_object.GetCurrentPattern(id_)
        return pattern_.QueryInterface(interface)

    def resolve_property(self, key):
        '''
        return resolved automation element property
        if reference properties does not contain requested key,
        raise not identified key exception
        '''
        try:
            return self._resolve_property(key)
        
        except AttributeError:
            return NotIdentifiedKey(key)

    def resolve_pattern(self, key):
        '''
        return resolved automation element pattern
        if reference patterns does not contain requested key,
        raise not identified key exception
        if reference patterns contains requested key,
        but automation element does not support reference pattern,
        raise not support key exception 
        '''
        try:
            return self._resolve_pattern(key)
        
        except AttributeError:
            return NotIdentifiedKey(key)

        except ValueError:
            return NotSupportedKey(key)

    def resolve_properties(self, *keys):
        '''
        return resolved automation element properties
        '''
        return {key: self.resolve_property(key) for key in keys}

    def resolve_patterns(self, *keys):
        '''
        return resolved automation element patterns
        '''
        return {key: self.resolve_pattern(key) for key in keys}

    def get_next_sibling_resolver(self):
        '''
        return next sibling resolver instance of this instance
        '''
        automation_object = self._tree_walker.GetNextSiblingElement(
            self._automation_object
            )
        
        if is_null_pointer(automation_object):
            return None
        
        else: 
            return self.__class__(automation_object)

    def get_first_child_resolver(self):
        '''
        return first child resolver instance of this instance
        '''
        automation_object = self._tree_walker.GetFirstChildElement(
            self._automation_object
            )
        
        if is_null_pointer(automation_object):
            return None
        
        else: 
            return self.__class__(automation_object)

    def get_parent_resolver(self):
        '''
        return parent resolver instance of this instance
        '''
        automation_object = self._tree_walker.GetParentElement(
            self._automation_object
            )
        
        if is_null_pointer(automation_object):
            return None
        
        else: 
            return self.__class__(automation_object)

    def iterate_on_sibling_resolvers(self):
        '''
        * root automation element has no sibling instance
        iterate all sibling resolver instances
        this method iterates silbing layer of this instance 
        '''
        next_resovler = self.get_next_sibling_resolver()

        while next_resovler is not None:
            yield next_resovler
            next_resovler = next_resovler.get_next_sibling_resolver()

    def iterate_on_child_resolvers(self):
        '''
        iterate all child resolver instances
        this method iterates first children layer of this instance 
        '''
        child_resolver = self.get_first_child_resolver()

        next_resovler = child_resolver
        while next_resovler is not None:
            yield next_resovler
            next_resovler = next_resovler.get_next_sibling_resolver()

    def iterate_on_parent_resolvers(self):
        '''
        * root automation element has no parent instance
        iterate all parent resolver instances
        this method iterates root vertical layer above this instance 
        '''
        parent_resolver = self.get_parent_resolver()

        while parent_resolver is not None:
            yield parent_resolver
            parent_resolver = parent_resolver.get_parent_resolver()
