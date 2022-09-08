"""
    iterate --> Consists of 3 important parts
        1.iteration==for-while
        2.iterable==list,dict,set,str,tuple,files,and anything have --iter--
        3.iterator==to the iterables on which we can implement next() or __next__
"""

# iteration:
# for i in range(1, 11):
#     print(i)

# iterable:
# what is __iter__ ?
# class Family:
#     def __init__(self):
#         self.names = ["Masoud", "Kimiya", "Hamide", "Saeid"]
#
#     def __iter__(self):
#         return iter(self.names)
#         # or
#         # for f_name in self.names:
#         #     yield f_name
#
#
# family_name = Family()
# for name in family_name:
#     print(f"My Family Name is: {name}")

# iterator:
# example 1
# nums = [1, 2, 3, 4, 5, 6]
# iter_nums = iter(nums)
# or
# iter_nums = nums.__iter__()
# print(next(iter_nums))
# or
# print(iter_nums.__next__())
# example 2
# name = "MasouD"
# iter_name = iter(name)
# print(next(iter_name))
# print(next(iter_name))
# print(next(iter_name))
# print(next(iter_name))
# print(next(iter_name))
# print(next(iter_name))
# example 3
# class Family:
#     def __init__(self):
#         self.names = ["Masoud", "Kimiya", "Hamide", "Saeid"]
#
#     def __iter__(self):
#         return iter(self.names)
#
#     def __next__(self):
#         names_copy = self.names
#         if names_copy:
#             return names_copy.pop()
#         else:
#             raise StopIteration
#
#
# family_name_copy = Family()
# print(next(family_name_copy))
# print(next(family_name_copy))
# print(next(family_name_copy))
# print(next(family_name_copy))
# print(next(family_name_copy))
