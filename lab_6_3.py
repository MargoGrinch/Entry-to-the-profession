# 3.
# Грінченко Маргарита 1 курс група 122Б
from enum import Enum

class Month(Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12

class Season(Enum):
    Winter = 1
    Spring = 2
    Summer = 3
    Autumn = 4

while True:
    while True:
        try:
            month = Month[input('month: ')]
            break
        except KeyError:
            print('wrong month')
    s = (month.value // 3 + 1) % 4
    print(Season(s))
    if input('Press "Enter" for continue') == '':
        continue
    break
