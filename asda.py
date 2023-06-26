# выписывает числа от а до b
def a2b(a, b):
    print(a)
    if a < b:
        a2b(a + 1, b)
    elif a > b:
        a2b(a - 1, b)

a2b(2, 213123)