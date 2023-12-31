# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума). Список
# можно задавать рандомно
#
# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

import random


def get_indexes(arr, low, high):
    return [arr.index(x) for x in arr if low <= x <= high]


if __name__ == '__main__':
    arr = [random.randint(1, 100) for _ in
           range(int(input('Please, input quantity of elements: ')))]
    print(arr)
    low = int(input('Please, input lower bound of range: '))
    high = int(input('Please, input upper bound of range: '))
    print(get_indexes(arr, low, high))
