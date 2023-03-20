

def summa_n(number):
    summ = 0
    for _ in range(1, number + 1):
        summ += _
    print('Я знаю, что сумма чисел от 1 до', number, 'равна', summ)

N = int(input('введите целое число '))
summa_n(N)
