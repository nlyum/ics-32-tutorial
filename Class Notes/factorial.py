def iter_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def rec_factorial(n): # the recursive function here uses more memory, since it uses more stack calls
    if n <= 1:
        return 1
    else:
        return n * rec_factorial(n-1)
    
if __name__ == "__main__":
    print(iter_factorial(5))
    print(rec_factorial(5))