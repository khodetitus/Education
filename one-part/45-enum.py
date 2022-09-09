import enum as en


# enum classes
@en.unique  # __> To avoid repeating values
class Days(en.Enum):  # or en.IntEnum:for using the integers and Compare values
    Monday = 0
    Sunday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    # Saturday = 9  # Error --> Keys should not be duplicated
    # Sunday12 = 1  # not be good since duplicated...
    # For times when we need automatic and non-repeating values:
    # Monday = en.auto()
    # Sunday = en.auto()
    # Tuesday = en.auto()
    # Wednesday = en.auto()
    # Thursday = en.auto()
    # Friday = en.auto()
    # Saturday = en.auto()


# compare values
# print(Days.Sunday > Days.Friday)

# order dict for enums:
for day, value in Days.__members__.items():
    print(day, value.value)

# print(Days.Sunday12 is Days.Sunday)

for days in Days:
    print(days)  # or print(days.value) or print(days.name)
print("-------------------------------------------------")
print(Days.Sunday)
print(repr(Days.Sunday))
print(Days.Sunday.value)
print(Days.Sunday.name)
print(type(Days.Sunday))
print(isinstance(Days.Sunday, Days))
print(Days(4))
# Days.Sunday = 8  # Error --> not be changed
