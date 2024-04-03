# Here is one of the worst practices in programming! The Global Variable!
z = 100  # z is global, and as such, it is visible by all other functions, and it can be modified!


def foo(a, b):
    a += 1
    b[0] += 5
    # Point 2
    global z
    z += 2


# bar()


def main():
    x = 10  # x and y are LOCAL variables to main
    y = [1, 2, 3]  # List is mutable, and as such,
    # It can be changed by the called function.
    # This is called pass by reference!
    # Point 1
    foo(x, y)
    print(x, y)
    # point 3
    bar()
    fun(10)
    # inside_function ()  # This doesn't work, because inside_function is only available inside of function fun!


def bar():
    a = 19
    # point 4
    print("z in bar is: ", z)  # z = 102
    print(a)  # 19


def fun(i):
    i *= 2
    print("in fun i is: ", i)

    def inside_function():  # nested function
        j = 10
        print("I am the inside function!", i, j)

    inside_function()

    # print("i and j in fun: ", i, j) #function fun, does not know j, because j only exists in the scope of the inside function


main()
