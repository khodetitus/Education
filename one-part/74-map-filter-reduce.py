# map
# example 1
list_of_names = ["masoud", "kimiya", "hamide", "saeid"]


def say_hello(name):
    return f"hello {name}"


for names in list_of_names:
    print(say_hello(names))
# or

for names in map(say_hello, list_of_names):
    print(names)
# or
print(list(map(say_hello, list_of_names)))
# example 2
numbers = (1, 2, 3, 4)
for nums in map(lambda x: x * x, numbers):
    print(nums)
# filter
# example 1
list_of_ages = [30, 25, 2, 18, 56, 45, 10, 5]


def filter_ages(age):
    if age > 20:
        return True


for ages in filter(filter_ages, list_of_ages):
    print(ages)

# example 2
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for nums in filter(lambda x: (x % 2 == 0), list_of_numbers):
    print("even of numbers is:", nums)

# reduce
from functools import reduce

list_of_nums = [2, 3, 5, 6]  # sum of numbers is 16


def add(a, b):
    return a + b


print("sum of numbers:", reduce(add, list_of_nums))  # without initial
# or
print("sum of numbers:", reduce(add, list_of_nums, 10))  # with initial
