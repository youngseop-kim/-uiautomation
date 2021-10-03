
import comtypes
import comtypes.client

UIAutomationCore = comtypes.client.GetModule(
    tlib='UIAutomationCore.dll'
    )

UIAutomationClient = comtypes.client.CreateObject(
    progid='{ff48dba4-60ef-4201-aa87-54103eef594e}', 
    interface=UIAutomationCore.IUIAutomation
    )

UIAutomationElementType = comtypes.POINTER(
    UIAutomationCore.IUIAutomationElement
    )

UIAutomationElementArrayType = comtypes.POINTER(
    UIAutomationCore.IUIAutomationElementArray
    )

UIAutomationUnknownType = comtypes.POINTER(
    UIAutomationCore.IUnknown
    )

class MustInheritError(Exception):
    
    def __init__(self, instance):
        subclasses = instance.__class__.__subclasses__()
        super().__init__(f'this class must inherit from {subclasses}')

class NotSupportedTypeError(Exception):

    def __init__(self):
        types = (UIAutomationElementType, UIAutomationElementArrayType,)
        super().__init__(f'this class supports only {types}')

class NotIdentifiedKey:

    def __init__(self, key):
        self._key = key

    def __str__(self):
        return f'[not identified "{self._key}"]'

    def __repr__(self):
        return f'[not identified "{self._key}"]'

class NotSupportedKey:

    def __init__(self, key):
        self._key = key

    def __str__(self):
        return f'[not supported "{self._key}"]'

    def __repr__(self):
        return f'[not supported "{self._key}"]'

def dumps_comobject(object_):
    return comtypes.string_at(
        comtypes.addressof(object_), 
        comtypes.sizeof(object_)
        )

def loads_comobject(comtype, bytes_):
    return comtype.from_buffer(
        bytearray(bytes_)
        )

def is_null_pointer(comtype):
    return comtypes.cast(comtype, comtypes.c_char_p).value is None