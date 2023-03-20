
def multipliers(a, b):
    result = a * b
    print(result)
def division(a, b):
    result = a / b
    print(result)
def summ(a, b):
    result = a + b
    print(result)
def subtraction(a, b):
    result = a - b
    print(result)

def calculator(do):
    match do:
        case '*':
            a = int(input('Введите число '))
            b = int(input('Введите число '))
            multipliers(a, b)
        case '/':
            a = int(input('Введите число '))
            b = int(input('Введите число '))
            division(a, b)
        case '+':
            a = int(input('Введите число '))
            b = int(input('Введите число '))
            summ(a, b)
        case '-':
            a = int(input('Введите число '))
            b = int(input('Введите число '))
            subtraction(a, b)


do = input('Введите действие "*", "/", "+", "-" ')
calculator(do)
