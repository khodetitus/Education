# creating dictionary in python with:
# 1
names_ages = {"masoud": 25, "kimiya": 23, "hamide": 31, "saeid": 35}
# # 2
names_ages2 = dict(masoud=25, kimiya=23, hamide=31, saeid=35)
print(names_ages)
print(names_ages2)
from collections import OrderedDict

name_order = OrderedDict(masoud=25, kimiya=23, hamide=31, saeid=35)
print(name_order)
# delete the last item with the following method:
name_order.popitem()  # by default last=True
print(name_order)

# delete the first item with the following method:
name_order.popitem(last=False)
print(name_order)

# move item to end item with using following method:
name_order.move_to_end("kimiya")  # by default last=True
print(name_order)

# move item to first item with using following method:
name_order.move_to_end("kimiya", last=False)
print(name_order)

name_order["shayan"] = 24
print(name_order)

# delete the item with using following method:
name_order.pop("shayan")
print(name_order)