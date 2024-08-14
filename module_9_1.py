def apply_all_func(int_list, *functions):
    result = {}
    for i in functions:
        result[i.__name__] = i(int_list)
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))