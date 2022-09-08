"""
In this example, we are going to measure the performance difference between generators and normal functions
"""


def normal_fibonacci(num):
    list_nums = []
    a, b = 0, 1
    while len(list_nums) < num:
        list_nums.append(b)
        a, b = b, a + b
    return list_nums


print(normal_fibonacci(10000000))


def generator_fibonacci(num):
    a, b = 0, 1
    count = 0
    while count < num:
        a, b = b, a + b
        yield b
        count += 1


for i in generator_fibonacci(10000000):
    print(i)
