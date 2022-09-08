# unpacking:
# example 1
my_list_info = ["masoud", 25, 185]


def show(name, age, height):
    print(name, age, height)


show(*my_list_info)

# example 2
my_dict_info = {"name": "masoud", "age": 25, "height": 185}


def show_information(name, age, height):
    print(name, age, height)


show_information(*my_dict_info)
show_information(**my_dict_info)
