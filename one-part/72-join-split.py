# join:
text = "hello, how are you????"
print(text.split(" "))
print(text.split(","))

# split:
# example 1
list_of_number = ['hello,', 'how', 'are', 'you????']
print(type(" ".join(list_of_number)))
print(" ".join(list_of_number))

# example 2
my_dict = {"name": "masoud", "age": "25"}
print(" ".join(my_dict.keys()))
print(" ".join(my_dict.values()))
