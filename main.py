


def my_pow(num1, degree):
    num_to_return = 1

    for i in range(degree):
        num_to_return *= num1

    return num_to_return


print(my_pow(15, 2))