"""
python class variables evaluation on declaration/import

"""
class A:
    def __init__(self) -> None:
        print("This is a class A")

class B:
    class_variable = A()