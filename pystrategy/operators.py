# TODO 
# Create custom comparison operators not present in stdlib operator module

import re

def between(a, b):

    # since reading from JSON, values are either string, float, or list of
    if not isinstance(b, list):
        raise ValueError('other value must be a list of length 2')
    
    return b[0] <= a <= b[1]

def in_(a, b):
    return a in b

def not_in(a, b):
    result = False if a in b else True
    return result

def not_contains(a, b):
    result = False if b in a else True
    return result

def re_contains(a, b):
    """Return True a regex search with pattern b yields a match in a

    Args:
        a (str): Pattern to search
        b (str): Regex pattern to use in search

    Returns:
        result (bool): Whether b contains a or not.
    """

    try:
        regexp = re.compile(b, flags=re.IGNORECASE)
    except(TypeError):
        raise TypeError('Value must be a string that can be compiled to regex expression')

    return bool(re.search(regexp, a))