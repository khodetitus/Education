# example 1
def first_number():
    yield 1
    yield 2
    yield 3


for i in first_number():
    print(i)


# example 2
def convert_number(num):
    number = 0
    while number < num:
        yield number
        number += 1


convert = convert_number(5)
print(next(convert))
print(next(convert))
print(next(convert))
print(next(convert))
print(next(convert))

# or
for i in convert_number(10):
    print(i)


# example 3
def generator_func():
    for num in range(10):
        yield num


number = generator_func()

print(next(number))
print(next(number))
print(next(number))
print(next(number))
# generator comprehension
generator_comp = (n for n in range(10))
