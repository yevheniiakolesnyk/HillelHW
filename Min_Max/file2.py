def min_own(*args, list_own=[]):
    list_own.append(args)

    def feature():
        v_min = float('inf')
        for el in list_own[0]:
            if el < v_min:
                v_min = el
        return v_min

    result = feature()
    return result


input_values = min_own(4, 8, 9, 1, 12, 88, 17, 77)
print(input_values)