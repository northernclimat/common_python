# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
import random


def min_flips(string_of_coins):
    heads = string_of_coins.count('H')
    tails = string_of_coins.count('T')
    return min(heads, tails)


if __name__ == '__main__':
    n = int(input('Please, input a quantity of coins'))  # quantity of coins
    coins = ''.join([random.choice(['H', 'T']) for _ in range(n)]) # T - tales, H - heads
    print(f'Your coins are {coins}, minimum flip is {min_flips(coins)}')

