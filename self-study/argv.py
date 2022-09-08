import sys

# example 1
print(sys.argv)
if sys.argv[1] == "admin":
    print("is good")
else:
    print("not found")

# example 2
print("This is the name of the program:", sys.argv[0])
print("Number of elements including the name of the program:", len(sys.argv))
print("Number of elements excluding the name of the program:", (len(sys.argv) - 1))
print("Argument List:", str(sys.argv))

# example 3

numbers = sys.argv[1:]
count = 0
if numbers:
    for i in numbers:
        count += int(i)
else:
    raise SyntaxError("You must enter integer")
grade = count / len(numbers)
print(grade)
