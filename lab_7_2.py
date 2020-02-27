# Дан текст з цифр і малих латинських літер, за яким слідує крапка. Визначити яких
# букв - голосних або приголосних більше в цьому тексті. Результат вивести на екран.
# Грінченко Маргарита Володимирівна 122 - Б
# 5 варіант
while True:
#    s = '01234567789zxcvbnmqwertyuiopasdfghjkl.'
    a = 'eyuia'
    b = 'qwrtpsdfghjklzxcvbnm'
    text = input("придумай текст: ")
    if text[-1] != ".":
        print("Where's dot?")
        continue
    turn = False
    count_of_a = 0
    count_of_b = 0
    for i in text:
        if i in a:
            count_of_a += 1
        if i in b:
            count_of_b += 1
        if i not in s:
            turn = True
    if turn:
        print("read the condition")
    if count_of_a > count_of_b:
        print("гласных больше")
    elif count_of_a < count_of_b:
        print("сoгласных больше")
    else:
        print("одинаковое количество")
    if input('Enter') == '':
        continue
    break
