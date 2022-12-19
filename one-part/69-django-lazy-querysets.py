class Person:
    def __init__(self) -> None:
        pass
    def objects(self):
        pass


class Car:
    def __init__(self) -> None:
        pass
    def objects(self):
        pass


p1 = Person.objects.get(id=2)
p2 = Person.objects.filter(name='john')
cars = Car.objects.order_by('speed')
cars.filter(name='benz')

# In all the above cases, none of the querysets were evaluated because they were not really needed to bring us information from the database.

"""
There are different methods to evaluate querysets

"""
#1.iteration
for p in Person.objects.all():
    print(p.name)

# 2.slicning
Person.objects.all()[:3]

#3.repr()
p1 = Person.objects.all()
repr(p1)

#4.len()
p = Person.objects.all()
len(p)

#5.list()
list(Person.objects.all())

#6.bool() or conditional
if Person.objects.filter(name='admin'):
    print('Hello admin...')
