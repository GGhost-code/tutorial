def mx(num):
    return max(mx(num[:-1]), int(num[-1])) if num else 0
print(mx('5354325325235'))