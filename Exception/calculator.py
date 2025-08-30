class InvalidFormulaException(Exception):
    pass
def evaluate(str):
    f = str.split()
    if f[1] == '+' or f[1] == '-' or f[1] == '*' or f[1] =='/':
        if f[1] == '+':
            res = int(f[0]) + int(f[2])
        elif f[1] == '-':
            res = int(f[0]) - int(f[2])
        if f[1] == '*':
            res = int(f[0]) * int(f[2])
        if f[1] == '/':
            if int(f[2]) != 0:
                res = int(f[0]) // int(f[2])
            else:
                raise ZeroDivisionError('Division by zero not allowed')
    else:
        raise InvalidFormulaException('Invalid formula')
    return res

str = input('enter formula: ')
try:
    ans = evaluate(str)
except (InvalidFormulaException, ZeroDivisionError, UnboundLocalError) as msg:
    print(msg)
else:
    print(ans)
finally:
    print('program ended successfully')