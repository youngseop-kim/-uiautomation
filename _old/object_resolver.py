
from base import ObjectResolver

class ObjectResolverForAutomationElement(ObjectResolver):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if not self._is_automation_element(self._object):
            raise TypeError

    def __str__(self):
        return f'{self.__class__.__name__}'

    def __repr__(self):
        return f'{self.__class__.__name__}'

    def _resolve_pattern(self, key):
        packed = self.reference_for_pattern[key]
        instance_id, instance_interface = packed
        instance_pattern = self._object.GetCurrentPattern(instance_id)
        return instance_pattern.QueryInterface(instance_interface)

    def _resolve_property(self, key):
        packed = self.reference_for_property[key]
        instance_id, instance_definition = packed
        instance_property = self._object.GetCurrentPropertyValue(instance_id)
        if instance_definition is not None:
            return instance_definition[instance_property]

        else:
            return instance_property

    def resolve_pattern(self, key):
        try:
            return self._resolve_pattern(key)

        except KeyError:
            return '[Not Identified Pattern]'
        
        except ValueError:
            return '[Not Supported Pattern]'

    def resolve_property(self, key):
        try:
            return self._resolve_property(key)
        
        except KeyError:
            return '[Not Identified Property]'

    def resolve_patterns(self, *keys):
        return {
            key : self.resolve_pattern(key)
            for key in keys
            }

    def resolve_properties(self, *keys):
        return {
            key : self.resolve_property(key)
            for key in keys
            }

    def iterate_on_siblings(self, tree_walker):
        next_object = tree_walker.GetNextSiblingElement(
            self._object
            )

        while not self._is_null_pointer(next_object):
            yield self.__class__.__base__.__subclass_from__(
                next_object
                )
                
            next_object = tree_walker.GetNextSiblingElement(
                next_object
                )
        
    def iterate_on_children(self, tree_walker):
        child_object = tree_walker.GetFirstChildElement(
            self._object
            )

        next_object = child_object
        while not self._is_null_pointer(next_object):
            yield self.__class__.__base__.__subclass_from__(
                next_object
                )
            
            next_object = tree_walker.GetNextSiblingElement(
                next_object
                )

    def iterate_on_parents(self, tree_walker):
        parent_object = tree_walker.GetParentElement(
            self._object
            )

        while not self._is_null_pointer(parent_object):
            yield self.__class__.__base__.__subclass_from__(
                parent_object
                )

            parent_object = tree_walker.GetParentElement(
                parent_object
                )
            
class ObjectResolverForAutomationElementArray(ObjectResolver):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if not self._is_automation_element_array(self._object):
            raise TypeError

    def __str__(self):
        return f'{self.__class__.__name__}<{self.__len__()}>'

    def __repr__(self):
        return f'{self.__class__.__name__}<{self.__len__()}>'

    def __len__(self):
        return self._object.Length

    def __getitem__(self, index):
        return self.__class__.__base__.__subclass_from__(
            self._object.GetElement(index)
            )

    def __iter__(self):
        for index in range(self.__len__()):
            yield self.__getitem__(index)

