# 1. За датою d, m, y визначити дату наступного і попереднього дня. В програмі врахувати наявність високосних років.
# Грінченко Маргарита 1 курс група 122Б

# def previous_day(day, month, year):
#     day -= 1
#     month -= 1
#     if day < 1:
#         month -= 1
#         day = months_list[month][1]
#     if month < 0:
#         year -= 1
#     previous_day = f'previous day: {day}:{months_list[month][0]}:{year}'


days = range(1, 32)
months = range(1, 13)
years = range(1901, 2020)
while True:
#перевірка умов
    while True:
        try:
            day = int(input('day: '))
            if day not in days:
                print('Try other number of day')
                continue
            
            month = int(input('months: '))
            if month not in months:
                print('Try other number of month')
                continue
            year = int(input('years: '))
            if year not in years:
                print('Try other number of year (1901-2020)')
                continue
            break    
        except ValueError:
            print('only digit')
#перевірка умов
            
    february = 28
    
    if year % 4 == 0:
        february = 29

    months_list = [['Январь', 31],
                   ['Февраль', february],
                   ['Март', 31],
                   ['Апрель', 30],
                   ['Май', 31],
                   ['Июнь', 30],
                   ['Июль', 31],
                   ['Август', 31],
                   ['Сентябрь', 30],
                   ['Октябрь', 31],
                   ['Ноябрь', 30],
                   ['Декабрь', 31]]

    if day > months_list[month - 1][1]:
        print('Different number of days')
        continue

    d, m, y = day, month, year
    d -= 1
    m -= 1
    if d < 1:
        m -= 1
        d = months_list[m][1]
    if m < 0:
        y -= 1
    previous_day = f'previous day: {d} - {months_list[m][0]} - {y}'

    d, m, y = day, month, year
    d += 1
    m -= 1
    if d > months_list[m][1]:
        m += 1
        d = 1
    if m > 11:
        m = 0
        y += 1
    next_day = f'next day: {d} - {months_list[m][0]} - {y}'

    print(previous_day)
    print(next_day)
    if input('Press "Enter" for continue: ') == '':
        continue
    break
