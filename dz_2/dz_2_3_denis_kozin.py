# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N


def print_powers_of_two(n):
    power = 1
    degrees = []
    while power <= n:
        if power:
            degrees.append(power)
        power *= 2
    return degrees


if __name__ == '__main__':
    n = int(input('Please, input a number N: '))
    degrees = [2 ** x for x in range(n + 1) if 2 ** x <= n]  # a lot of unnecessary calculations
    print(degrees)
    print(print_powers_of_two(n))
