stack = []
a = input()
bad = False
for i in a:
    if i == "(" or i == "[":
        stack.append(i)
    else:
        if len(stack) == 0:
            bad = True
            break
        if stack[-1] == "(" and i != "]" or stack[-1] == "[" and i != ")":
            stack.pop()
        else:
            bad = True
            break

if len(stack) != 0:
    bad = True

if bad:
    print("Неправильно")
else:
    print("Правильно")