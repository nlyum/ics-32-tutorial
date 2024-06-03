def sum_of_digits(x):
    if x == 0:
        return 0
    return x % 10 + sum_of_digits(x//10)

if __name__ == "__main__":
    print(sum_of_digits(555))