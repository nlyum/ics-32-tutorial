def __verify_int(n):
    try:
        test_var = int(n)
    except ValueError:
        raise ValueError("The Mathseries module only works with integers!")
    else:
        return n

# this is a higher order function that will create any function to
# calculate the sum of a series
def series_sum_factory(series_term):
    def series(max_n):
        total_sum = 0
        i = 1
        tested_max_n = __verify_int(max_n)
        while i <= tested_max_n:
            total_sum += series_term(i)
            i += 1
        return total_sum
    return series

if __name__ == "__main__":
    sum_numbers = series_sum_factory(lambda x : x)
    sum_squares = series_sum_factory(lambda x : x * x)
    sum_cubes = series_sum_factory(lambda x : x * x * x)

    result = sum_numbers(3)
    print(result)