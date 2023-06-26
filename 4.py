def stepen(n):
    return stepen(n / 2) if n > 4 else False if n % 2 != 0 and n != 1 else True

def stepen2(n):
    return stepen2(n // 2) if n > 4 else False if n % 2 != 0 and n != 1 else True

if stepen(int(input())):
    print("Является")
else:
    print("Не является")