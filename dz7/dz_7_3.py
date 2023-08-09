import easygui


def check_rhythm(verse):
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    phrases = verse.split()

    if len(phrases) <= 1:
        return "Парам пам-пам"

    count = sum(1 for letter in phrases[0] if letter in vowels)

    for phrase in phrases[1:]:
        if count != sum(1 for letter in phrase if letter in vowels):
            return "Пам парам"

    return "Парам пам-пам"


def multiplication_table(num_rows=6, num_columns=6):
    table = ""
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            table += str(i * j) + "\t"
        table += "\n"
    return table


while True:
    menu_choice = easygui.buttonbox("Выберите задачу:",
                                    choices=["Ритм стиха", "Таблица умножения", "Выход"])

    if menu_choice == "Ритм стиха":
        verse = easygui.enterbox("Введите стих:")
        if verse:
            result = check_rhythm(verse)
            easygui.msgbox(result, "Результат")

    elif menu_choice == "Таблица умножения":
        dimensions = easygui.multenterbox("Введите размеры таблицы:",
                                          fields=["Количество строк", "Количество столбцов"])
        if dimensions:
            rows, columns = map(int, dimensions)
            table = multiplication_table(rows, columns)
            easygui.textbox("Таблица умножения:", text=table)

    else:
        break
