

def NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    gcd = a + b
    print(gcd)

a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
NOD(a, b)