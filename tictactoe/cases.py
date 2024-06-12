cases = {
    'line': ['top', 'center', 'bottom'],
    'column': ['left', 'middle', 'right']
}

casesKeys = {typeCmd: ', '.join(cases[typeCmd]) for typeCmd in cases}


def getLines():
    return cases['line']

def getColumns():
    return cases['column']

def getLinesKeys():
    return casesKeys['line']

def getColumnsKeys():
    return casesKeys['column']

def getCase(typeCmd='', value=''):
    """
    Returns the index of the specified type and value.
    
    Raises ValueError if value is not present.
    """
    typeCases = cases.get(typeCmd)
    if typeCases is None:
        raise ValueError(f'Error: typeCmd ({typeCmd}) must be "line" or "column"')
    
    try:
        return typeCases.index(value)
    except ValueError:
        raise ValueError(f'Error: {typeCmd} ({value}) must be one of {casesKeys.get(typeCmd)}')

def getLine(value='center'):
    """Returns the index of the specified line value."""
    return getCase('line', value)

def getColumn(value='middle'):
    """Returns the index of the specified column value."""
    return getCase('column', value)

# Example usage
# try:
#     print(getLine('top'))      # Output: 0
#     print(getLine('center'))   # Output: 1
#     print(getLine('bottom'))   # Output: 2
#     print(getLine('invalid'))  # Should raise an error
# except ValueError as e:
#     print(e)

# try:
#     print(getColumn('left'))    # Output: 0
#     print(getColumn('middle'))  # Output: 1
#     print(getColumn('right'))   # Output: 2
#     print(getColumn('invalid')) # Should raise an error
# except ValueError as e:
#     print(e)