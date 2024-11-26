roc_grad = [2, 5, 9, 6, 7, 2]
def talirg(dong):
    for i in range(len(dong) - 1, 0, -1):
        for j in range(i):
            if dong[j] > dong[j + 1]:
                dong[j], dong[j + 1] = dong[j + 1], dong[j]
    return dong
print(talirg(roc_grad))


def sasirg(dong):
    for i in range(len(dong) - 1):
        mas_index = i
        for j in range(i + 1, len(dong)):
            if dong[mas_index] > dong[j]:
                mas_index = j
                dong[mas_index], dong[j] = dong[j], dong[mas_index]
    return dong
print(sasirg(roc_grad))

def urand(dong):
    for i in range(1, len(dong)):
        kais = dong[i]
        j = i - 1
        while dong[j] > kais and  j >= 0:
            dong[j + 1] = dong[j]
            j -= 1
        dong[j + 1] = kais
