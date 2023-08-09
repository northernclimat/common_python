def count_vowels(s):
    vowels = 'аеёиоуыэюя'
    return sum(1 for char in s if char in vowels)


def has_rhythm(poem):
    phrases = poem.split()
    if len(set(count_vowels(phrase) for phrase in phrases)) == 1:
        return "Парам пам-пам"
    return "Пам парам"


poem = input()
print(has_rhythm(poem))
