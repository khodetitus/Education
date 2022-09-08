# example 1
# normal functions
def add(x, y):
    return x + y


print(add(5, 10))

# lambda functions
add = lambda x, y: x + y
print(add(5, 10))

# example 2
x = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9]


# normal functions
def multiply(number):
    return number * number


print(list(map(multiply, x)))

# lambda functions
print(list(map(lambda i: i * i, x)))

# example 3

list_of_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# normal functions
def even_numbers(number):
    if number % 2 == 0:
        return True


print(list(filter(even_numbers, list_of_number)))
# lambda functions
print(list(filter(lambda x: x % 2 == 0, list_of_number)))

# example 4
list_of_tuples = [(4, "b"), (2, "a"), (5, "c"), (1, "e"), (3, "d")]
print(sorted(list_of_tuples, key=lambda x: x[1]))
