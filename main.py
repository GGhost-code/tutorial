stack = []
stack2 = []
a = input() + " "
c = 0
num = ""
while True:
    while True:
        i = a[c]
        c += 1
        if (ord('1') > ord(i) or ord(i) > ord('9')) and c != 1:
            break
        num += i
    stack.append(int(num))
    if i == " ":
        break
    stack2.append(i)
    num = ""
c = 0
for i in range(len(stack2)):
    if stack2[i] == "*":
        a1 = stack.pop(i - c)
        a2 = stack.pop(i - c)
        stack.insert(i - c, a1 * a2)
        c += 1
    elif stack2[i] == "/":
        a1 = stack.pop(i - c)
        a2 = stack.pop(i - c)
        stack.insert(i - c, a1 // a2)
        c += 1
c = 0
for i in range(len(stack2)):
    if stack2[i] == "+":
        a1 = stack.pop(0)
        a2 = stack.pop(0)
        stack.insert(0, a1 + a2)
    elif stack2[i] == "-":
        a1 = stack.pop(0)
        a2 = stack.pop(0)
        stack.insert(0, a1 - a2)

print(stack[0])
