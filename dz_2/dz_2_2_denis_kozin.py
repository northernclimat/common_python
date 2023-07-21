# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по
# математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
import math


def katya_check_1(addition: int, multiplication: int):
    desc = (addition ** 2 - 4 * multiplication)
    if desc < 0:
        return None
    else:
        x1 = (addition + math.sqrt(desc)) / 2
        x2 = (addition - math.sqrt(desc)) / 2
        return x1, x2


def katya_check_2(addition: int, multiplication: int):
    for i in range(1, addition):
        j = addition - i
        if i * j == multiplication:
            return i, j
    return None


if __name__ == '__main__':
    addition = int(input('Please, input your addition: '))
    multiplication = int(input('Please, input your multiplication: '))
    if not katya_check_2(addition, multiplication):
        print('no solution')
    else:
        print(katya_check_2(addition, multiplication))
    if not katya_check_1(addition, multiplication):
        print('no solution')
    else:
        print(katya_check_1(addition, multiplication))

