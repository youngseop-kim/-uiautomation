
from definition.resolver import Resolver
from definition.resolver import ResolverFactory
from definition.resolver_guide import ResolverGuideExpression
from definition.resolver_guide import ResolverGuide

import reference.patterns
import reference.properties

Resolver._reference_properties = reference.properties
Resolver._reference_patterns = reference.patterns

root = ResolverFactory.create_instance_from_root()
expression = {
    'name' : '1Code',
    '__match_method' : 'is_match_fnmatch'
    }

expression_ = ResolverGuideExpression(expression)
resolver_ = ResolverGuide.point_horizontally(
    root,
    expression_.public_expression,
    expression_.private_expression
    )

print(resolver_.resolve_property('name'))