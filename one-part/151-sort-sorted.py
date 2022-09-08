# sorted
# example 1
name = "masoud"
print(sorted(name))
# example 2
list_of_names = ["masoud", "amir", "kimiya", "hamide", "saeid"]
print(f"original list is : {list_of_names}")
print(f"sorted list is : {sorted(list_of_names)}")
print(f"sorted reverse list is : {sorted(list_of_names, reverse=True)}")
# sort by len character
print(f"sort by character length is : {sorted(list_of_names, key=len)}")
# sort by char 2
print(f"sort by character second is : {sorted(list_of_names, key=lambda x: x[1])}")
print(f"sort by character second and reverse list is : {sorted(list_of_names, key=lambda x: x[1], reverse=True)}")
# example 3
numbers = (1, 2, 34, 4, 5, 9, 6)
print(sorted(numbers))
print(sorted(numbers, reverse=True))
print(sorted(numbers))

# sort
list_of_names = ["masoud", "amir", "kimiya", "hamide", "saeid", "Shayan"]
list_of_names.sort()
print(list_of_names)
