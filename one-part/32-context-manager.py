# using the context manager with built-in function"open":
with open("akbar.txt", "w") as f:
    f.write("hello akbar chetori dadash?")


# creating a context manager:
# example 1
class Greeting:
    def __enter__(self):
        print("Welcome To Python!!")

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Nice To See You!!!!")


def say_hello(name):
    print(f"Hello {name} How Are You?")


with Greeting():
    say_hello("MasouD")


# example 2

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with FileManager("akbar.txt", "w") as f:
    f.write("salam akbar dadash")


# example 3

class Product:
    def __init__(self, name: str, inventory: int):
        self.name = name
        self.inventory = inventory

    def __repr__(self):
        return f"Product: {self.name}\nInventory: {self.inventory}$"


class Order:
    def __init__(self, product: Product, amount: int):
        self.product = product
        self.amount = amount

    def payment(self, name_card: str, card_number: int, cvv2: int, password: int):
        pass

    def __enter__(self):
        self.product.inventory -= self.amount
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.product.inventory += self.amount
            print(f"Error:{exc_type=} : {exc_val=}")
        else:
            print("Congratulations!!")
        return True


obj1 = Product("Orange", 10000)
print(obj1)
with Order(obj1, 20) as f:
    print(obj1)
    f.payment("Blue Bank", 1234123, 204, 1818)
print(obj1)
