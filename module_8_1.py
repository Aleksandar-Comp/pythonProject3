def add_everything_up(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result =  a + b
        elif isinstance(a, str) and isinstance(b, str):
            result = a + b
        elif isinstance(a, str) and isinstance(b, (int, float)):
            result = a + str(b)
        elif isinstance(a, (int, float)) and isinstance(b, str):
            result = str(a) + b
    except TypeError as g:
        print(g)
        result = str(a) + str(b)
    return result




print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
