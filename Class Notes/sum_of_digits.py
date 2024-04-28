def rec_digit_sum(n):
    if n < 10:
        return n
    else:
        return (n % 10) + rec_digit_sum(n // 10)

def iter_digit_sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

if __name__ == "__main__":
    x = 1370958731
    print(rec_digit_sum(x))
    print(iter_digit_sum(x))