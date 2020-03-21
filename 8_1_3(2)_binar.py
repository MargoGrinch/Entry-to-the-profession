"""
Бінарний пошук підрядка
Грінченко Маргарита Володимирівна 122
"""
import numpy as np

while True:
    print("Бинарный поиск: \n")
    quesh = input(
    get = input("Ввести данные самостоятельно - 'yes', иначе рандом\n")
    if get == 'yes':
        while True:
            try:
                g = int(input())
                #ввод длины массива
                x = int(input())
                #выделяем память под массив
                break
            except ValueError:
                print('Только числа !')
        a = np.zeros(g, dtype=int)
        print("Введите массив: ")
        for i in range(g):
            while True:
                try:
                    a[i] = int(input("Введите число: "))
                    break
                except ValueError:
                    print('Только числа !')
        print(a)
        #искомый элемент
        a.sort()
        #сортировка массива
        g = len(a)
        print(a)
        i = 0
        L = 0
        R = g - 1
        flag = True
        counter_def = 0
        while L <= R and flag:
            i += 1
            K = (L + R) // 2
            if g[K] == g:
                counter_def += 2
                print(g, 'Найдено на первой позиции - ', K)
                print('количество совпадений - ', counter_def)
                flag = False
            elif a[K] < x:
                counter_def += 3
                L = K + 1
            elif a[K] > x:
                counter_def += 4
                R = K - 1
        if flag:
            print(x, 'Не найдено !')
            print('Количество:', counter_def)
    else:
        #когда элемент не присутсвует в массиве
        a = [1, 2, 3, 4, 5, 6, 2, 3, 4, 52, 5, 1, 4124, 5, 6, 72, 21]
        a = np.array(a)
        x = 15
        #искомый элемент
        a.sort()
        # сортировка массива
        g = len(a)
        print(a)
        i = 0
        L = 0
        R = g - 1
        flag = True
        counter_def = 0
        while L <= R and flag:
            i += 1
            K = (L + R) // 2
            if g[K] == g:
                counter_def += 2
                print(g, 'Найдено на первой позиции - ', K)
                print('количество совпадений - ', counter_def)
                flag = False
            elif a[K] < x:
                counter_def += 3
                L = K + 1
            elif a[K] > x:
                counter_def += 4
                R = K - 1
        if flag:
            print(x, 'Не найдено !')
            print('Количество:', counter_def)

        # Искомый элемент присутсвует в массиве
        a = [1, 2, 3, 4, 5, 6, 2, 3, 4, 52, 5, 1, 4124, 5, 6, 72, 21]
        a = np.array(a)
        x = 6
        # искомый элемент
        a.sort()
        # сортировка массива
        g = len(a)
        print(a)
        i = 0
        L = 0
        R = g - 1
        flag = True
        counter_def = 0
        while L <= R and flag:
            i += 1
            K = (L + R) // 2
            if g[K] == g:
                counter_def += 2
                print(g, 'Найдено на первой позиции - ', K)
                print('количество совпадений - ', counter_def)
                flag = False
            elif a[K] < x:
                counter_def += 3
                L = K + 1
            elif a[K] > x:
                counter_def += 4
                R = K - 1
        if flag:
            print(x, 'Не найдено !')
            print('Количество:', counter_def)
            
    if input('Что бы продолжить, введите пустую строку: ') == '':
        continue
    break
