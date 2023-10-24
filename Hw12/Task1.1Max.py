def max_own(*args, list_own=[]):
    list_own.append(args)

    def feature():
        v_max = float('-inf')
        for el in list_own[0]:
            if el > v_max:
                v_max = el
        return v_max

    result = feature()
    return result


print(max_own(4, 8, 9, 1, 12, 88, 17, 77, 177))

def logger(func):
    def wrapper():
        result = func.__name__
        return result

    return wrapper()


print(logger(max_own))