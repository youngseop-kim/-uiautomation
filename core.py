
import definition.resolver
import reference.patterns
import reference.properties

definition.resolver.Resolver._reference_properties = reference.properties
definition.resolver.Resolver._reference_patterns = reference.patterns

a = definition.resolver.ResolverFactory.create_instance_from_root()
for i in a.iterate_on_child_resolvers():
    for j in i.iterate_on_child_resolvers():
        print(j.resolve_patterns('text', 'window'))