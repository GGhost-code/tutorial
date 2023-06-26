def sum():
    a = int(input())
    return sum() + a if a else a
print(sum())
