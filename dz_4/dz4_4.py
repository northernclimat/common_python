def add_polynomials(pol_f, pol_s):
    first = pol_f.copy()

    for power, co in pol_s.items():
        if power in first:
            first[power] += co
        else:
            first[power] = co

    first = {power: coeff for power, coeff in first.items() if coeff != 0}

    return first


def poly_to_string(poly):
    terms = []

    for power, co in sorted(poly.items(), key=lambda item: item[0], reverse=True):
        if co == 0:
            continue
        elif power == 0:
            terms.append(str(co))
        elif power == 1:
            terms.append(f"{'' if co == 1 else co}x")
        else:
            terms.append(f"{'' if co == 1 else co}x^{power}")

    return " + ".join(terms).replace("+ -", "- ")


if __name__ == "__main__":
    poly1 = {2: 2, 1: 4, 0: 5}  # 2x^2 + 4x + 5
    poly2 = {3: 5, 2: -3, 0: -12}  # 5x^3 - 3x^2 - 12

    result = add_polynomials(poly1, poly2)
    result_str = poly_to_string(result)

    print(result_str)  # value: 5x^3 - x^2 + 4x - 7
