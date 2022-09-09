# normal function
def show(name):
    return f"hello {name},how are you?"


print(show("masoud"))


# example 1
# generator function
def show2(name):
    yield f"hello {name},how are you?"
    yield "good morning"


for text in show2("masoud"):
    print(text)


# example 2
def positive_number(number):
    num = 0
    while num < number:
        yield num
        num += 1


for i in positive_number(10):
    print(i)


# example 3
def reverse_positive_number(number):
    print("Starting....")
    while number > 0:
        yield number
        number -= 1


for numbers in reverse_positive_number(10):
    print(numbers)
# or
generator_var = reverse_positive_number(10)
print(next(generator_var))
print(next(generator_var))
print(next(generator_var))

# example 4
# list comprehensions
even_numbers = [numbers for numbers in range(1, 10) if numbers % 2 == 0]
print(even_numbers)

# generator comprehensions
generator_even_numbers = (numbers for numbers in range(1, 10) if numbers % 2 == 0)
for i in generator_even_numbers:
    print(i)
# or
print(next(generator_even_numbers))
print(next(generator_even_numbers))
print(next(generator_even_numbers))
print(next(generator_even_numbers))
# example 5
import sys

# performance list comprehensions with get size of
list_numbers = [i * 2 for i in range(1000000)]
print(sys.getsizeof(list_numbers))
# performance generator comprehensions with get size of
generator_numbers = (i * 2 for i in range(1000000))
print(sys.getsizeof(generator_numbers))

# example 6
import cProfile

# performance list comprehensions with cprofile
cProfile.run("sum([i*2 for i in range(1000000)])")
# performance generator comprehensions with cprofile
cProfile.run("sum((i*2 for i in range(1000000)))")
