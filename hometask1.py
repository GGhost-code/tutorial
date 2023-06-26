def recurseCalc(expression):
    print("Called:", expression)
    if len(expression) == 0:
        return 0
    number = ''
    i = 0
    print()
    while expression[i].isnumeric():
        number += expression[i]
        i += 1
        if i >= len(expression):
            print("broke")
            break
    print("i ==", i)

    if '+' in expression[i:]:
        return recurseCalc(expression[:expression.rfind("+")]) + recurseCalc(expression[expression.rfind("+") + 1:])
    elif '-' in expression[i:]:
        return recurseCalc(expression[:expression.rfind("-")]) - recurseCalc(expression[expression.rfind("-") + 1:])
    elif '*' in expression[i:]:
        return recurseCalc(expression[:expression.rfind("*")]) * recurseCalc(expression[expression.rfind("*") + 1:])
    elif '/' in expression[i:]:
        return recurseCalc(expression[:expression.rfind("/")]) / recurseCalc(expression[expression.rfind("/") + 1:])
    else:
        print("Number returned")
        return int(number)

print(recurseCalc('1/2*4/5'))