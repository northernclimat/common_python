def round_to_double_zero(number):  # we should round to 2 zero in a row
    multiplier = 1
    while True:
        temp_number = round(number * multiplier, 2)
        if temp_number * 100 % 100 == 0:
            return temp_number / multiplier
        multiplier *= 10


def sum_of_digits(number):
    number = abs(number)
    int_part = int(number)
    fractional_part = round_to_double_zero(number - int_part)

    summarize = 0
    while int_part >= 1:
        summarize += int_part % 10
        int_part //= 10

    while fractional_part > 0:
        fractional_part *= 10
        digit = int(fractional_part)
        summarize += digit
        fractional_part -= digit  # getting rid of the fractional part we already used

    return summarize


print(sum_of_digits(123.45))
