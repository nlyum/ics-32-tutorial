def count_even_digits(n):
    if n % 2 == 0:
        even_digit = 1
    else:
        even_digit = 0
    if n < 10:
        return even_digit
    else:
        return even_digit + count_even_digits(n // 10)


if __name__ == "__main__":
    print(count_even_digits(31421342))