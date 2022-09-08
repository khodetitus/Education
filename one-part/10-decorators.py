# # 1.Creating Decorators
# # syntax:
def outer(func):
    def inner():
        pass

    return inner


@outer
def func():
    pass


print(func())


#
# # example 1
def outer_upper(func):
    def inner_upper():
        f = func()
        text = f.upper()
        return text

    return inner_upper


@outer_upper
def show():
    return "hello world!!!"


print(show())


#
# # 2.applying multiple decorators to a single functions
def outer_upper(func):
    def inner_upper():
        f = func()
        text = f.upper()
        return text

    return inner_upper


def outer_split(func):
    def inner_split():
        f = func()
        text = f.split(" ")
        return text

    return inner_split


@outer_split
@outer_upper
def show():
    return f"hello world!!!"


print(show())


# 3.accepting arguments in decorator functions
def outer_upper(func):
    def inner_upper(show_name):
        f = func(show_name)
        text = f.upper()
        return text

    return inner_upper


@outer_upper
def say_hello(name):
    return f"hello {name},how are you?"


print(say_hello("masoud"))


# 4.defining general purpose decorators
def outer_upper(func):
    def inner_upper(show_name, *args, **kwargs):
        print(args)
        print(kwargs)
        f = func(show_name)
        text = f.upper()
        return text

    return inner_upper


@outer_upper
def say_hello(name):
    return f"hello {name},how are you?"


print(say_hello("masoud", "kimiya", age_masoud=25, age_kimiya=23))


# 5.passing arguments to the decorator
def outer_arg(name, family):
    def outer_upper(func):
        def inner_upper(t):
            print(name, family)

            f = func(t)
            text = f.upper()
            return text

        return inner_upper

    return outer_upper


@outer_arg("masoud", "zandi")
def show(text):
    return text


print(show("hello world"))

# 6.debugging decorators
import functools


def outer_arg(name, family):
    def outer_upper(func):
        @functools.wraps(func)
        def inner_upper(t):
            'Inner Upper function'
            print(name, family)

            f = func(t)
            text = f.upper()
            return text

        return inner_upper

    return outer_upper


@outer_arg("masoud", "zandi")
def show(text):
    'show function'
    return text


print(show.__name__)
print(show.__doc__)
