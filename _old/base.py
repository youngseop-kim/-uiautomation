
import comtypes
import comtypes.client

UIAutomationClient = comtypes.client.GetModule(
    'UIAutomationCore.dll'
    )

UIAutomation = comtypes.client.CreateObject(
    progid = UIAutomationClient.CUIAutomation._reg_clsid_,
    interface = UIAutomationClient.IUIAutomation,
    )

UIAutomationUnknownClass = comtypes.POINTER(
    UIAutomationClient.IUnknown
    )

UIAutomationElementClass = comtypes.POINTER(
    UIAutomationClient.IUIAutomationElement
    )

UIAutomationElementArrayClass = comtypes.POINTER(
    UIAutomationClient.IUIAutomationElementArray
    )

class MustSubclassError(Exception):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ObjectResolver(object):
    '''base object resolver class'''
    
    reference_for_class = None
    reference_for_pattern = None
    reference_for_property = None

    def __init__(self, object_):
        if self.__class__.__base__ == object:
            raise MustSubclassError

        self._object = object_

    def _stand_by_for_pickle_dumps(self):
        self._object = self.__dump_from__(self._object)

    def _stand_by_for_pickle_loads(self):
        self._object = self.__load_from__(self._object)
        
    @classmethod
    def __subclass_from__(cls, object_):
        subclasses = cls.__subclasses__()
        subclass_name = cls.reference_for_class[object_.__class__.__name__][1]
        
        for subclass in subclasses:
            if subclass.__name__ == subclass_name: 
                return subclass(object_)
    
    @classmethod
    def __dump_from__(cls, object_):
        object_class = object_.__class__.__name__.encode()
        object_field = comtypes.string_at(
            comtypes.addressof(object_), 
            comtypes.sizeof(object_)
            )
        
        return object_class + b'__dump_from__' + object_field

    @classmethod
    def __load_from__(cls, object_):
        object_class, object_field = object_.split(b'__dump_from__')
        
        return cls.reference_for_class[object_class.decode()][0].from_buffer(
            bytearray(object_field)
            )

    @classmethod
    def _is_unknown(cls, object_):
        return isinstance(object_, UIAutomationUnknownClass)

    @classmethod
    def _is_automation_element(cls, object_):
        return isinstance(object_, UIAutomationElementClass)

    @classmethod
    def _is_automation_element_array(cls, object_):
        return isinstance(object_, UIAutomationElementArrayClass)

    @classmethod
    def _is_query_interface_available(cls, object_):
        return hasattr(object_, 'QueryInterface')
    
    @classmethod
    def _is_null_pointer(cls, object_):
        return comtypes.cast(object_, comtypes.c_char_p).value is None
        
class ObjectResolverReference(object):
    '''base object resolver reference class'''
    
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            instance = super(cls.__class__, cls).__new__(cls)
            cls._instance = instance
            
        return cls._instance

    def __init__(self):
        if self.__class__.__base__ == object:
            raise MustSubclassError

        self._object = {}
        
    def __setitem__(self, key, value):
        self._object[key] = value
        
    def __getitem__(self, key):
        return self._object[key]

    def __str__(self):
        return str(self._object)

    def __repr__(self):
        return repr(self._object)

    def keys(self):
        return self._object.keys()

    def values(self):
        return self._object.values()

    def items(self):
        return self._object.items()
        
    