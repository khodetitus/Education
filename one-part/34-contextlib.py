import contextlib


# using context manager with built-in decorator
@contextlib.contextmanager
def show(name):
    print(f"{name},Welcome to Python !!!")  # __enter__
    yield {}  # Everything inside the "with" indent is replaced here!!
    print(f"{name},Nice to see you !!!")  # __exit__


# single call
with show("MasouD") as s:
    print("Hello")
    # multi call
with show("masoud") as m, show("kimiya") as k, show("saeid") as a:
    print("Hello")  # in __exit__ is reversed sort inputs.


# creating decorator with using contextDecorator
class CreatDecorator(contextlib.ContextDecorator):
    def __enter__(self):
        print("Starting....")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting...")


@CreatDecorator()
def say_hello():
    print("Hello")


say_hello()
