def age_assignment(*args, **kwargs):
    result = {}
    for name in args:
        for k, v in kwargs.items():
            if name[0] == k:
                result[name] = v
    return result
