# any:
# example 1
my_list = [False, 0]
print(any(my_list))

# example 2
my_list_2 = [False, 0, 4]
print(any(my_list_2))

# example 3
indy_500_2018_john = {
    'driver_name': 'John Appleseed',
    'race_year': 2018
}

print(any(indy_500_2018_john))

# example 4
top_10_ranking = ""
print(any(top_10_ranking))

# all:
# example 1
my_llist_all = [1, 2, 3, True, "masoud"]
print(all(my_llist_all))

# example 2
my_llist_all_2 = [1, True, 0, False]
print(all(my_llist_all_2))
