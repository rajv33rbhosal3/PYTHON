def multiply_n_iterations(a, b):
    result = 0
    for _ in range(b):
        result += a
    return result


result = multiply_n_iterations(5, 3)
print("Result using N iterations:", result)
