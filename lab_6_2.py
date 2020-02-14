# 3.
# Грінченко Маргарита 1 курс група 122Б

from enum import Enum

class converter (Enum):
    USD = 1
    EUR = 2
    CZK = 3
    PLN = 4

while True:
    while True:
        try:
            x = float (input ( 'amount of money:'))
            if (x > 4 or x < 1):
                print('wrong amount of money')
                continue
            p = converter [input ( 'currency:')]
            break
        except (KeyError, ValueError):
            print('Error')
            
    if p.name == converter(1).name:
        UAH = x * 24.52
        print(UAH)
    elif p.name == converter(2).name:
        UAH = x * 26.6
        print(UAH)
    elif p.name == converter(3).name:
        UAH = x * 1.07
        print(UAH)
    elif p.name == converter(4).name:
        UAH = x * 6.27
        print(UAH)
        
            
    if input('Press "Enter" for continue') == '':
        continue
    break
