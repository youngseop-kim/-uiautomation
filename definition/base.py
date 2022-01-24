
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