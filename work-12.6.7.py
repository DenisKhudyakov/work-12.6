import random
def rock_paper_scissors():
  # Здесь будет игра «Камень, ножницы, бумага»
  choosingRobot = ['Камень', 'Ножницы', 'Бумага']
  you_win = 0
  robot_win = 0
  while you_win < 3 and robot_win < 3:
    # Играем до трёх побед
    randomСhoice = random.choice(choosingRobot)
    yourChoice = input('Камень, ножницы, бумага. Раз, Два, Три: ')
    print('Выбор робота', randomСhoice)
    if yourChoice.__eq__('бумага') and randomСhoice.__eq__('Камень'):
      print('Вы выиграли')
      you_win += 1
    elif yourChoice.__eq__('бумага') and randomСhoice.__eq__('Ножницы'):
      print('Робот выиграл')
      robot_win += 1
    elif yourChoice.__eq__('камень') and randomСhoice.__eq__('Ножницы'):
      print('Вы выиграли')
      you_win += 1
    elif yourChoice.__eq__('камень') and randomСhoice.__eq__('Бумага'):
      print('Робот выиграл')
      robot_win += 1
    elif yourChoice.__eq__('ножницы') and randomСhoice.__eq__('Бумага'):
      print('Вы выиграли')
      you_win += 1
    elif yourChoice.__eq__('ножницы') and randomСhoice.__eq__('Камень'):
      print('Робот выиграл')
      robot_win += 1
    elif yourChoice.__eq__(randomСhoice):
      continue
    else:
      print('Ошибка ввода')
      continue


def guess_the_number():
  # Здесь будет игра «Угадай число»
  number1 = int(random.uniform(0, 20.0))
  attempt = 0
  while True:
    answer = int(input('Угадайте число от 0 до 20: '))
    attempt += 1
    if answer < number1:
      print('Число меньше, чем нужно. Попробуйте ещё раз!')
    elif answer > number1:
      print('Число больше, чем нужно. Попробуйте ещё раз!')
    else:
      print('Красавчик! Количество попыток:', attempt)
      break

def mainMenu():
  message = (input('Выберите игру. \nКамень ножницы бумага, кнопка "1" \nУгадай число кнопка "2" '))
  if message.__eq__('2'):
    guess_the_number()
    mainMenu()
  elif message.__eq__('1'):
    rock_paper_scissors()
    mainMenu()
  else:
    print('Ошибка ввода')


mainMenu()
