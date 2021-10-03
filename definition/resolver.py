
from reference.base import MustInheritError
from reference.base import NotSupportedTypeError

from reference.base import NotIdentifiedKey
from reference.base import NotSupportedKey

from reference.base import dumps_comobject
from reference.base import loads_comobject
from reference.base import is_null_pointer

from reference.base import UIAutomationClient
from reference.base import UIAutomationUnknownType
from reference.base import UIAutomationElementType
from reference.base import UIAutomationElementArrayType

def is_unknown_type(automation_object):
    return isinstance(automation_object, UIAutomationUnknownType)
    
def is_automation_element_type(automation_object):
    return isinstance(automation_object, UIAutomationElementType)

def is_automation_element_array_type(automation_object):
    return isinstance(automation_object, UIAutomationElementArrayType)

def is_query_interface_available(automation_object):
    return hasattr(automation_object, 'QueryInterface')

def is_supported_type(automation_object):
    condition = [
        is_automation_element_type(automation_object),
        is_automation_element_array_type(automation_object)
        ]
    
    return any(condition)

def raise_exception_unless_subclass(method):
    # decorator
    def decorated(self, *args, **kwargs):
        if self.__class__.__bases__[0] == object:
            raise MustInheritError(self)

        return method(self, *args, **kwargs)
    return decorated

def raise_exception_unless_supported_type(method):
    # decorator
    def decorated(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        if not is_supported_type(self._automation_object):
            raise NotSupportedTypeError()

        return result
    return decorated

class ResolverFactory(object):

    def __new__(cls, automation_object):
        return cls.create_instance(automation_object)

    @classmethod
    def create_instance(cls, automation_object):
        if is_automation_element_type(automation_object):
            return AutomationElementResolver(automation_object)

        elif is_automation_element_array_type(automation_object):
            return cls.create_instances_from_array(automation_object)
        
        else:
            raise NotSupportedTypeError()

    @classmethod
    def create_instances_from_array(cls, automation_object):
        array = tuple()
        for index in range(automation_object.Length):
            array+=(cls(automation_object.GetElement(index)),)

        return array
    
    @classmethod
    def create_instance_from_root(cls):
        return cls(UIAutomationClient.GetRootElement())

class Resolver(object):

    _tree_walker = UIAutomationClient.RawViewWalker
    _automation_object = None

    _reference_properties = None
    _reference_patterns = None

    @raise_exception_unless_supported_type
    @raise_exception_unless_subclass
    def __init__(self, automation_object):
        self._automation_object = automation_object

    @raise_exception_unless_subclass
    def _ready_for_pickle_dumps(self):
        self._automation_object = dumps_comobject(
            object_ = self._automation_object
            )
    
    @raise_exception_unless_subclass
    def _ready_for_pickle_loads(self):
        self._automation_object = loads_comobject(
            comtype = UIAutomationElementType, 
            bytes_ = self._automation_object
            )

class AutomationElementResolver(Resolver):

    def __str__(self):
        return str(self.__class__.__name__)

    def __repr__(self):
        return repr(self.__class__.__name__)

    def _resolve_property(self, key):
        id_ = getattr(self._reference_properties, key)
        property_ = self._automation_object.GetCurrentPropertyValue(id_)
        return property_
        
    def _resolve_pattern(self, key):
        id_, interface = getattr(self._reference_patterns, key)
        pattern_ = self._automation_object.GetCurrentPattern(id_)
        return pattern_.QueryInterface(interface)

    def resolve_property(self, key):
        try:
            return self._resolve_property(key)
        
        except AttributeError:
            return NotIdentifiedKey(key)

    def resolve_pattern(self, key):
        try:
            return self._resolve_pattern(key)
        
        except AttributeError:
            return NotIdentifiedKey(key)

        except ValueError:
            return NotSupportedKey(key)

    def resolve_properties(self, *keys):
        return {key: self.resolve_property(key) for key in keys}

    def resolve_patterns(self, *keys):
        return {key: self.resolve_pattern(key) for key in keys}

    def get_next_sibling_resolver(self):
        automation_object = self._tree_walker.GetNextSiblingElement(
            self._automation_object
            )
        
        if is_null_pointer(automation_object):
            return None
        
        else: 
            return self.__class__(automation_object)

    def get_first_child_resolver(self):
        automation_object = self._tree_walker.GetFirstChildElement(
            self._automation_object
            )
        
        if is_null_pointer(automation_object):
            return None
        
        else: 
            return self.__class__(automation_object)

    def get_parent_resolver(self):
        automation_object = self._tree_walker.GetParentElement(
            self._automation_object
            )
        
        if is_null_pointer(automation_object):
            return None
        
        else: 
            return self.__class__(automation_object)

    def iterate_on_sibling_resolvers(self):
        next_resovler = self.get_next_sibling_resolver()

        while next_resovler is not None:
            yield next_resovler
            next_resovler = next_resovler.get_next_sibling_resolver()

    def iterate_on_child_resolvers(self):
        child_resolver = self.get_first_child_resolver()

        next_resovler = child_resolver
        while next_resovler is not None:
            yield next_resovler
            next_resovler = next_resovler.get_next_sibling_resolver()

    def iterate_on_parent_resolvers(self):
        parent_resolver = self.get_parent_resolver()

        while parent_resolver is not None:
            yield parent_resolver
            parent_resolver = parent_resolver.get_parent_resolver()
