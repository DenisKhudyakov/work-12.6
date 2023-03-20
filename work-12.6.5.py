
def count_letters(text):
    symbol = input('какую букву ищем? ')
    number = int(input('Какую цифру ищем? '))
    count_sumbol = 0
    count_number = 0
    for i in text:
        if i.__eq__(symbol):
            count_sumbol += 1
        elif i.__eq__(str(number)):
            count_number += 1
    print('Количество букв', symbol + ':', count_sumbol)
    print('Количество цифр', str(number) + ':', count_number)



count_letters('Введите текст: 100 лет в обед')