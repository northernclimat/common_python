# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность
# и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии:
# an = a1 + (n-1) * d. Каждое число вводится с новой строки.

def main():
    a1 = int(input('Please, input first number: '))
    d = int(input('Please, input progression difference: '))
    n = int(input('Please, input a quantity of progression elements: '))
    lisf_of_progression = [a1]
    for i in range(1, n):
        lisf_of_progression.append(lisf_of_progression[i-1] + d)
    return lisf_of_progression


if __name__ == '__main__':
    print(main())
