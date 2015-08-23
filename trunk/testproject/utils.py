def ObjectToDict(o):
    return dict((str.lower(key), value) for key, value in vars(o).iteritems() 
                 if not callable(value) and not key.startswith('__'))