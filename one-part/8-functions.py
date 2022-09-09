# 1.functions are object:
def show(name):
    return f"hello {name}"


y = show()  # callable
# or
x = show
print(x("masoud"))  # without callable
# or
print(show("masoud"))


# 2.functions can be sorted in datat structure:
def show(name):
    return f"hello {name.upper()}"


data_structre = [show, str.capitalize, str.lower]
for names in data_structre:
    print(names("mAsOud"))

# or
print(data_structre[0]("masoud"))
print(data_structre[1]("mAsOud"))
print(data_structre[2]("mAsOud"))


# 3.functions can be passed to other functions (higher_order functions):
# example 1
def show(name):
    return f"hello {name}"


def shoot(func):  # higher-order functions
    return func("masoud")


print(shoot(show))


# example 2
def show(name):
    return f"hello {name}"


func = map(show, ["masoud", "kimiya", "hamide"])  # map is higher-order functions
for names in func:
    print(names)


# 4.function can be nested (inner and outer functions):
# example 1
def show():
    def say_hello(name):
        return f"hello {name}"

    print(say_hello("masoud"))


show()


# example 2
def show(name):  # nested functions
    def shoot(n):
        return f"hello {n}"

    print(shoot(name))


show("masoud")


# example 3
def person(age):  # outer function
    def adult(name):  # inner function
        return f"{name} is adult!!"

    def kid(name):  # inner function
        return f"{name} is kid!"

    if age > 18:
        return adult
    else:
        return kid


age_person = person(25)
print(age_person("masoud"))


# 5.function can capture local state (lexical closure):
def person(age, name):
    def adult():  # lexical closure
        return f"{name} is adult!!"

    def kid():  # lexical closure
        return f"{name} is kid!"

    if age > 18:
        return adult


#     else:
#         return kid


person_age = person(25, "masoud")
print(person_age())  # callable


# 6.objects can behave like functions
# example 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"{self.name} is {self.age} years old!")


object_person = Person("masoud", 25)
object_person()  # object_person is not callable and not function


# example 2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        print(f"{self.name} is {self.age} years old!")


object_person = Person("masoud", 25)
object_person()  # object_person is callable and is functions
