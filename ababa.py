def sum(n):
    return sum(n[:-1]) + int(n[-1]) if n else 0

def sum2(n):
    if n == 0:
        return 0
    return sum(n // 10) + n % 10

def reverse(n):
    return n[-1] + reverse(n[0:-1]) if n else ""

print(reverse("12345678"))