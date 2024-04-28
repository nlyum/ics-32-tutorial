def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def calculate(a, b, calculating_func):
    return calculating_func(a, b)

if __name__ == "__main__":
    result_1 = calculate(10, 20, add)
    result_2 = calculate(10, 20, multiply)

    print(result_1)
    print(result_2)
