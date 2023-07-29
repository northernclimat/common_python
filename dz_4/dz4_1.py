"""Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без
повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. Пользователь
вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств

"""


def common_elements():
    n = int(input("please, input a quantity of elements in the first set: "))
    set_one = set()
    for i in range(n):
        element = int(input(f"Input element {i + 1} of the first set: "))
        set_one.add(element)

    m = int(input("\nplease, input a quantity of elements in the second set: "))
    set_two = set()
    for i in range(m):
        element = int(input(f"Input element {i + 1} of the second set: "))
        set_two.add(element)

    set_one.update(set_two)
    common = sorted(list(set_one))
    return ' '.join([str(x) for x in common])


if __name__ == '__main__':
    print(common_elements())
