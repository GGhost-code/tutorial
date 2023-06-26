def zv(n):
 if not n:
  return ""
 return n[0] + '*' + zv(n[1:]) if len(n) != 1 else n[0]
print(zv(input()))