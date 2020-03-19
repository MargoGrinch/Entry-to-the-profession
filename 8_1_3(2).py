'''
2. Задача полягає у вивченні і реалізації алгоритмів пошуку для даних, підготовлених
за допомогою функції моделювання випадкових чисел і текстів, підготовлених
самостійно.
Для кожного алгоритму необхідно підготувати тести, що підтверджують
працездатність програми. Для всіх алгоритмів пошуку повинні бути приведені лістинги
програм пошуку та лістинги результатів (номера позиції в вихідному масиві, починаючи
з якого розташований елемент або фрагмент пошуку; кількості порівнянь по кожному
алгоритму пошуку).
Найпростіші алгоритми пошуку:
 лінійний пошук;
 бінарний пошук;
 прямий пошук підрядка.
Грінченко Маргарита Володимирівна 122
'''
import numpy as np
while True:
    print("лінійний пошук:\n")
    A = np.random.randint(0, 11, 24)
    print("масив:")
    print(A)
    i = 0
    count = 0
    while i < 24 and A[i] != 11:
        i += 1
        count += 1
    if i == 24:
        print('Елемент', 11, 'не знайдений')
        print('Кількість порівнянь:', count)
    else:
        count += 1
        print('Елемент', 11, 'вперше зустричається у позиції', i)
        print('Кількість порівнянь:', count)

    A = np.random.randint(0, 8, 24)
    A[-1] = 3
    print("random number array :")
    print(A)
    i = 0
    count = 0
    while i < 24 and A[i] != 3:
        i += 1
        count += 1
    if i == 24:
        print('Елемент', 3, 'не знайдений.')
        print('Кількість порівнянь:', count)
    else:
        count += 1
        print('Item', 3, 'first found in position', i)
        print('Кількість порівнянь:', count)

    print("\nбінарний пошук:\n")
    a = np.random.randint(0, 20, 24)
    A[-1] = 11
    a.sort()
    print("масив:")
    print(a)
    i = 0
    L = 0
    R = 23
    K = 0
    flag = True

    while L <= R and flag:
        i += 1
        K = (L + R) // 2
        if a[K] == 11:
            print('Елемент', 11, 'вперше зустричається у позиції', K)
            print('Кількість порівнянь:', i)
            flag = False
        elif a[K] < 11:
            L = K + 1
        elif a[K] > 11:
            R = K - 1
    if flag:
        print('Елемент', 11, 'не знайдений.')
        print('Кількість порівнянь:', i)
    print()

    a = np.random.randint(0, 10, 24)
    a.sort()
    print("масив:")
    print(a)
    i = 0
    L = 0
    R = 23
    K = 0
    flag = True

    while L <= R and flag:
        i += 1
        K = (L + R) // 2
        if a[K] == 11:
            print('Елемент', 11, 'вперше зустричається у позиції', K)
            print('Кількість порівнянь:', i)
            flag = False
        elif a[K] < 11:
            L = K + 1
        elif a[K] > 11:
            R = K - 1
    if flag:
        print('Елемент', 11, 'не знайдений.')
        print('Кількість порівнянь:', i)

    print("\nпрямий пошук підрядка:\n")
    text = "мам мама мам мила раму"
    pattern = "мила"
    i = -1
    j = 0
    count = 0
    print('Текст:', text)
    print('Підрядок:', pattern)
    while (j < len(pattern)) and i < (len(text) - len(pattern)):
        j = 0
        i += 1
        while j < len(pattern) and pattern[j] == text[i + j]:
            j += 1
            count += 1
    if j == len(pattern):
        print('Підрядок знайдений в позиції', i)
    else:
        print('Елемент не знайдений.')
    print('Кількість порівнянь', count)
    print()
    text = "мам мама мам мила раму"
    pattern = "мила кота, але він втік"
    i = -1
    j = 0
    count = 0
    print('Текст:', text)
    print('Підрядок:', pattern)
    while (j < len(pattern)) and i < (len(text) - len(pattern)):
        j = 0
        i += 1
        while j < len(pattern) and pattern[j] == text[i + j]:
            j += 1
            count += 1
    if j == len(pattern):
        print('Підрядок знайдений в позиції', i)
    else:
        print('Елемент не знайдений.')
    print('Кількість порівнянь', count)

    if input('Введіть пустий рядок, щоб перезапустити') == '':
        continue
    break
