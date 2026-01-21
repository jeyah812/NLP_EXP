def plural(noun):
    if noun.endswith('y'):
        return noun[:-1] + 'ies'
    elif noun.endswith(('s', 'x', 'ch', 'sh')):
        return noun + 'es'
    else:
        return noun + 's'

print(plural("city"))