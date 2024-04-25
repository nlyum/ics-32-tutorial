def divide(a, b):
    try: 
        return a / b
    except ZeroDivisionError:
        print(f"Can't divide by zero!")
    finally:
        pass

if __name__ == "__main__":
    print(divide(10, 0))