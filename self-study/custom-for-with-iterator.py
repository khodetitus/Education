def custom_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break


my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
custom_for(my_numbers)
