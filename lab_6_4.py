# 4. Робота світлофора для водіїв запрограмована таким чином: на початку кожної години протягом трьох хвилин горить зелений сигнал, потім протягом однієї
#хвилини - жовтий, протягом двох хвилин - червоний, протягом трьох хвилин - знову зелений і т. д.
# Розробити програму, яка вводить дійсне число t, що означає час в хвилинах, що минув з початку чергової години і визначає сигнал якого кольору горить
#для водіїв в цей момент.
# Грінченко Маргарита 1 курс група 122Б

while True:
    while True:
        try:
            time = float(input('time: '))
            break
        except ValueError:
            print('only float')
    time %= 6
    if time < 3:
        print("green")
    elif time < 4:
        print("yellow")
    else:
        print("red")
    if input('Press "Enter" for continue ') == '':
        continue
    break
