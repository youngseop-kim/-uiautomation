
from base import UIAutomation
from base import UIAutomationClient

from object_resolver import *
from object_resolver_reference import *

import ctypes
import ctypes.wintypes

ObjectResolver.reference_for_class = ObjectResolverReferenceForClass()
ObjectResolver.reference_for_pattern = ObjectResolverReferenceForPattern()
ObjectResolver.reference_for_property = ObjectResolverReferenceForProperty()

def main():
    ex_name = None
    name = None

    while True:
        cursor_point = ctypes.wintypes.tagPOINT()
        ctypes.windll.user32.GetCursorPos(ctypes.byref(cursor_point))
        object_ = UIAutomation.ElementFromPoint(cursor_point)
        object_resolver = ObjectResolver.__subclass_from__(object_)
        
        name = object_resolver.resolve_property('name')
        if ex_name == name:
            pass

        else:
            print(f'"{name}"', flush=True)
            ex_name = name

    print('>>', object_resolver.resolve_property('name'))
    
    
    for i in object_resolver.iterate_on_parents(UIAutomation.RawViewWalker):
        print(i.resolve_property('name'))
    print('x')

main()