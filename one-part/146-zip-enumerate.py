# zip
list1 = ["masoud", "kimiya", "saeid", "hamide", "shayan"]
list2 = [25, 23, 35, 30]
result = zip(list1, list2)
print(list(result))
# or
for i in zip(list1, list2):
    print(i)

# enumerate
list_enum = ["akbar", "asghar", "ali", "mopalmo"]
result_enum = enumerate(list_enum)
print(list(result_enum))
for n, i in enumerate(list_enum):
    print(f"{n} = {i}")
