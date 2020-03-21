"""
Прямий пошук підрядка
Грінченко Маргарита Володимирівна 122
"""
import numpy as np
while True:
    print("Прямой поиск подстроки: \n")
    get = input("Ввести данные самостоятельно - 'yes', иначе рандом\n")
    if get == 'yes':
        text = input("Введите строку")
        pattern = input("Введите подстроку, которую нужно найти")
        i = -1ы
        j = 0
        count = 0
        print('Текст:', text)
        print('Подстрока:', pattern)
        while (j < len(pattern)) and i < (len(text) - len(pattern)):
            count += 2
            j = 0
            i += 1
            while j < len(pattern) and pattern[j] == text[i + j]:
                count += 2
                j += 1
        if j == len(pattern):
            print('Подстрока на позиции', i)
        else:
            print('Не найдено')
        print('Количество сравнений - ', count)
    else:
        # Ищем подстроку которая присутсвует в строке
        text = "мам мам мама мыла раму"
        pattern = "мыла"
        i = -1
        j = 0
        count = 0
        print('Текст:', text)
        print('Подстрока:', pattern)
        while (j < len(pattern)) and i < (len(text) - len(pattern)):
            count += 2
            j = 0
            i += 1
            while j < len(pattern) and pattern[j] == text[i + j]:
                count += 2
                j += 1
        if j == len(pattern):
            print('Подстрока на позиции', i)
        else:
            print('Не найдено')
        print('Количество сравнений - ', count)
        print()
        text = "мам мам мама мыла раму"
        pattern = "мыла кота, но он убежал"
        i = -1
        j = 0
        count = 0
        print('Текст:', text)
        print('Подстрока:', pattern)
        while (j < len(pattern)) and i < (len(text) - len(pattern)):
            count += 2
            j = 0
            i += 1
            while j < len(pattern) and pattern[j] == text[i + j]:
                count += 2
                j += 1
        if j == len(pattern):
            print('Подстрока на позиции', i)
        else:
            print('Не найдено')
        print('Количество сравнений', count)
    if input('Что бы продолжить, введите пустую строку: ') == '':
        continue
    break
