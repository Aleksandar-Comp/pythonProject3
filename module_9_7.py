def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        sum_ = sum(args)
        k = 0
        for i in range(2, sum_ // 2 + 1):
            if sum_ % i == 0:
                k = k + 1
        if k <= 0:
            print('Простое')
        else:
            print('Сщставное')
        return result
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)

