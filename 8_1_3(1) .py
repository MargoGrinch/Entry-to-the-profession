'''
1. Напишіть програми, що виконують такі операції з масивами (використовувати
вбудовані методи по роботі з масивами заборонено):
 виведіть на екран елементи лінійного масиву (заданий користувачем) у
зворотному порядку;
 виведіть на екран транспоновану матрицю 3*3 (початкова матриця задана
користувачем).
 виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність.
Результати множення елементів занесіть до нової матриці та виведіть її на екран;
 у матриці 4*4, що задана користувачем замініть всі від’ємні елементи на 0.
Грінченко Маргарита Володимирівна 122
'''
import numpy as np
print("press 1 for reverse\npress 2 for transp\npress 3 for multiply\npress 4 for exchange all elements 0\n")
while True:
    try:
        num = int(input("your number = "))
        #считываем номер выполненной программы           
    except ValueError:
        print('only digit 1, 2, 3 or 4')
        #проверяем на ошибку (кроме цифер ничего вводить нельзя)
    if (num == 1):
        print("your martrix is linear !")
        lenght = int(input())
        matrix = np.zeros((lenght, 1), dtype=int)
        #выделяем место для массива 
        new_matrix = np.zeros((lenght, 1), dtype=int)
        #выделяем место для массива
        i = 0
        for i in range(lenght):
            matrix[i, 0] = int(input())
            #пользователь заполняет масиив данными
        count = lenght - 1
        #для того что бы идти с конца, создаю переменную что бы в массиве передать конечный параметр (минус один потому что последний элемент не включительно)
        for i in range(lenght):
            new_matrix[i, 0] = matrix[count, 0]
            #заполняю новый массив данными из начального но с конечного значения
            count -= 1
            #что бы массив заполнялся новыми данными, надо идти по начальному (с конца)
        print("first version")
        print(matrix)
        print("reverse result")
        print(new_matrix)


    elif(num == 2):
        print('default size of your matrix 3x3')
        matrix = np.zeros((3, 3), dtype = int)
        #выделяем место для массива
        new_matrix = np.zeros((3, 3), dtype = int)
        #выделяем место для массива
        i, j = 0, 0
        for i in range(3):
            for j in range(3):
                matrix[i, j] = int(input())
                #пользователь заполняет масиив данными
        for i in range(3):
            for j in range(3):
                new_matrix[i, j] = matrix[j, i]
                #присваиваем столбцы начального массива строчкам созданного и наоборот (транспонованная матрица) 
        print(f'matrix before\n{matrix}')
        print(f'matrix after\n{new_matrix}')
             

    elif(num == 3):
        print('default size both of your matrix 3x3')
        A = np.zeros((3, 3), dtype = int)
        #выделяем место для массива
        B = np.zeros((3, 3), dtype = int)
        #выделяем место для массива
        C = np.zeros((3, 3), dtype = int)
        #выделяем место для массива
        i, j = 0, 0
        for i in range(3):
            for j in range(3):
                A[i, j] = int(input())
        #пользователь заполняет масиив данными       
        i, j = 0, 0
        for i in range(3):
            for j in range(3):
                B[i, j] = int(input())
        #пользователь заполняет масиив данными        
        i, j = 0, 0
        for i in range(3):
            for j in range(3):
                C[i, j] = A[i, 0] * B[0, j] + A[i, 1] * B[1, j] + A[i, 2] * B[2, j]
            #формула для умножения одной матрицы на другую (выведена непосредственно личными наблюдениями за закономерностью)
        print("first matrix")
        print(A)
        print("second mtrix")
        print(B)
        print("result matrix")
        print(C)

        
    elif(num == 4):
        print('default size both of your matrix 4x4')
        matrix = np.zeros((4, 4), dtype = int)
        i, j = 0, 0
        for i in range(4):
            for j in range(4):
                matrix[i, j] = int(input())
                if (matrix[i, j] < 0):
                    matrix[i, j] = 0
                    #проверка условия, если элемент меньше 0, заменяем его на 0
        print(matrix)
    else:            
        continue
    if input('Enter') == '':
        continue
    break

