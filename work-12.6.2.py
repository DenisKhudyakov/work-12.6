
def positive():
    print('Положительное')
def negative():
    print('Отрицательное')
def test(number = int(input('Введите целов число '))):
    if number > 0:
        positive()
    else:
        negative()


test()

