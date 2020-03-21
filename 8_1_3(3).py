'''
Виконайте добуток двох квадратних матриць n*n, врахуйте розмірність.
Результати множення елементів занесіть до нової матриці та виведіть її на екран;
Грінченко Маргарита Володимирівна 122
'''
import numpy as np
while True:
    try:
        size = int(input("size of your matrix = "))
    except ValueError:
        print("only digits")

    A_matrix = np.zeros((size, size), dtype = int)
    #выделение памяти под массив
    B_matrix = np.zeros((size, size), dtype = int)
    #выделение памяти под массив
    mult_matrix = np.zeros((size, size), dtype = int)
    #выделение памяти под массив

    for i in range(size):
        for j in range(size):
            A_matrix[i, j] = int(input())
            #считываем данные для первого массива
    
    for i in range(size):
        for j in range(size):
            B_matrix[i, j] = int(input())
            #считываем данные для второго массива
    
    
    i, j, count, summa = 0, 0, 0, 0
    for i in range (size) :
        for j in range (size):
            for count in range (size) :
                summa += A_matrix[i][count]*B_matrix[count][j]
                #создам переменную которая будет обсчитывать для каждого элемента его значение
            mult_matrix[i][j] = summa
            #записываем в наш элемент массива его значение
            summa = 0
            #обнуляем что бы обсчет следующего элемента начался с 0
    print(mult_matrix)
    
    if input('Enter') == '':
        continue
    break
