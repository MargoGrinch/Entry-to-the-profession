"""
Лінійний пошук підрядка
Грінченко Маргарита Володимирівна 122
"""
import numpy as np

while True:
    print("Линейный поиск: \n")
    get = input("Ввести данные самостоятельно - 'yes', иначе рандом\n")
    if get == 'yes':
        while True:
            try:
                g = int(input())
                #ввод длины массива
                x = int(input())
                #ввод искомого элемента
                break
            except ValueError:
                print('only digit')
        a = np.zeros(g, dtype=int)
        print("Ввод массива:")
        for i in range(g):
            while True:
                try:
                    a[i] = int(input("Введите целое число: "))
                    break
                except ValueError:
                    print("Только числа !")
        print(a)
        # линейный поиск
        i = 0
        g = len(a)
        count = 0
        while i < g and a[i] != x:
            count += 2
            i += 1
        if i == g:
            print(x, 'Не найдено')
            print('Количество - ', count)
        else:
            print(x, 'Найдено на такой позиции: ', i)
            print('Количество - ', count)
    else:
        #не найдено в массиве
        a = [1, 2, 3, 4, 5, 6, 2, 3, 4, 52, 5, 1, 4124, 5, 6, 72, 21]
        a = np.array(a)
        x = 15
        #искомый элемент
        print(a)
        i = 0
        g = len(a)
        count = 0
        while i < g and a[i] != x:
            count += 2
            i += 1
        if i == g:
            print(x, 'Не найдено')
            print('Количество - ', count)
        else:
            print(x, 'Найдено на такой позиции: ', i)
            print('Количество - ', count)

        #найдено в массиве
        a = [1, 2, 3, 4, 5, 6, 2, 3, 4, 52, 5, 1, 4124, 5, 6, 72, 21]
        a = np.array(a)
        x = 6
        #искомый элемент
        print(a)
        i = 0
        g = len(a)
        count = 0
        while i < g and a[i] != x:
            count += 2
            i += 1
        if i == g:
            print(x, 'Не найдено')
            print('Количество - ', count)
        else:
            print(x, 'Найдено на такой позиции: ', i)
            print('Количество - ', count)
            
    if input('Что бы продолжить, введите пустую строку: ') == '':
        continue
    break
