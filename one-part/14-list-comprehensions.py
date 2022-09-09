# example 1
# Even numbers between 1 and 20 with using normal list:
list_of_even_number = []
for i in range(1, 21):
    if i % 2 == 0:
        list_of_even_number.append(i)
print(f"my list of even number : {list_of_even_number}")
# example 2
# Even numbers between 1 and 20 with using comprehensions list:
comp_list_of_even_number = [i for i in range(1, 21) if i % 2 == 0]
print(f"my comprehensions list of even number : {comp_list_of_even_number}")
# example 3
# number % 2,5 ==0 numbers between 1 and 20 with using comprehensions list:
comp_list = [i for i in range(1, 21) if i % 2 == 0 if i % 5 == 0]
print(f"my comprehensions list : {comp_list}")

# example 4
# even or odd list:
even_or_odd_list = [(i, "even" if i % 2 == 0 else "odd") for i in range(1, 11)]
print(f"my comprehensions even or odd list : {even_or_odd_list}")
