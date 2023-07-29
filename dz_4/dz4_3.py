def convert_base(n: int, base: int) -> str:
    if base not in [2, 8]:
        raise ValueError("Base must be 2 or 8")

    if n == 0:
        return "0"

    digits = []
    while n:
        digits.append(str(n % base))
        n //= base

    return ''.join(digits[::-1])


def to_binary(n: int) -> str:
    return convert_base(n, 2)


def to_octal(n: int) -> str:
    return convert_base(n, 8)


if __name__ == "__main__":
    n = 192
    print(to_binary(n))  # >>> 101010
    print(bin(n)[2:])  # checking >>> 101010
    print(to_octal(n))  # >>> 52
    print(oct(n)[2:])  # checking >>> 52
