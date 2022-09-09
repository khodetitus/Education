# isinstance:
# example 1
name = "masoud"
print(isinstance(name, str))
print(isinstance(name, int))

# example 2
age = 25
print(isinstance(age, str))
print(isinstance(age, int))
print(isinstance(age, (tuple, list, str, int, dict)))


# example 3
class A:
    pass


a = A()
print(isinstance(a, A))


# example 4
class A(str):
    pass


a = A()
print(isinstance(a, str))


# issubclass
# example 1
class A:
    pass


class B(A):
    pass


print(issubclass(B, A))
print(issubclass(A, B))


# example 2
class A(str):
    pass


class B(A):
    pass


print(issubclass(B, str))
