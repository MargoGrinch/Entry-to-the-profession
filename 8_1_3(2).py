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
    print(" лінійний пошук:\n")
    A = np.random.randint(0, 11, 24)
    print("random number array :")
    print(A)
    i = 0
    count = 0
    while i < 24 and A[i] != 11:
        i += 1
        count += 1
    if i == 24:
        print('Item', 11, 'not found.')
        print('number of comparisons:', count)
    else:
        print('Item', 11, 'first found in position', i)
        print('number of comparisons:', count)

    A = np.random.randint(0, 8, 24)
    print("random number array :")
    print(A)
    i = 0
    count = 0
    while i < 24 and A[i] != 3:
        i += 1
        count += 1
    if i == 24:
        print('Item', 3, 'not found.')
        print('number of comparisons:', count)
    else:
        print('Item', 3, 'first found in position', i)
        print('number of comparisons:', count)
    print("\n бінарний пошук:\n")

    print("\n прямий пошук підрядка:\n")
    if input('Input "Enter" for restart') == '':
        continue
    break
