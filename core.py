
from definition.resolver import Resolver
from definition.resolver import ResolverFactory
from definition.resolver_guide import ResolverGuideExpression
from definition.resolver_guide import ResolverGuide

import definition.patterns
import definition.properties

Resolver._reference_properties = definition.properties
Resolver._reference_patterns = definition.patterns

root = ResolverFactory.create_instance_from_root()
expression = {
    'name' : '*Windows 메모장',
    '__resolve_method' : 'resolve_property',
    '__match_method' : 'is_match_fnmatch',
    '__max_depth' : -1,
    '__max_recursion_depth' : 1000,
    }

expression_ = ResolverGuideExpression(expression)

resolvers = ResolverGuide.iterate_with_breadth_first_search(
    root,
    expression_.public_expression,
    expression_.private_expression
    )

for resolver_ in resolvers:
    print(resolver_)
    print(resolver_.resolve_property('name'))