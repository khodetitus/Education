# recursive
# example 1
def fn():
    # ...
    fn()
    # ...


# example 2
def count_down(start_number):
    print(start_number)
    start_number -= 1
    if start_number > 0:
        count_down(start_number)


count_down(20)


# example 3
def sum(n):
    if n > 0:
        return n + sum(n - 1)
    return 0


print(sum(20))


# example 4
def fact(number):
    if number == 0:
        return 1
    else:
        return number * fact(number - 1)


print(fact(5))

# How does the fact work?
# answer:
# lets walk through the execution.
# fact(5):
#    5 is not 0, so fact(5) = 5 * fact(4)
#    what is fact(4)?
# fact(4):
#    4 is not 0, so fact(4) = 4 * fact(3)
#    what is fact(3)?
# fact(3):
#    3 is not 0, so fact(3) = 3 * fact(2)
#    what is fact(2)?
# fact(2):
#    2 is not 0, so fact(2) = 2 * fact(1)
#    what is fact(1)?
# fact(1):
#    1 is not 0, so fact(1) = 1 * fact(0)
#    what is fact(0)?
# fact(0):
#    0 IS 0, so fact(0) is 1

# Now lets gather our result.
#
# fact(5) = 5* fact(4)
# substitute in our result for fact(4)
#
# fact(5) = 5 * 4 * fact(3)
# substitute in our result for fact(3)
#
# fact(5) = 5 * 4 * 3 * fact(2)
# substitute in our result for fact(2)
#
# fact(5) = 5 * 4 * 3 * 2 * fact(1)
# substitute in our result for fact(1)
#
# fact(5) = 5 * 4 * 3 * 2 * 1 * fact(0)
# substitute in our result for fact(0)
#
# fact(5) = 5 * 4 * 3 * 2 * 1 * 1 = 120

# And there you have it. Recursion is the process of breaking a larger problem down by looking at it as
# successfully smaller problems until you reach a trivial (or "base") case.

# answer2
# fact(5)
# | 5  * fact(4)
# || 5 * (4 * fact(3))
# ||| 5 * (4 * (3 * fact(2))
# |||| 5 * (4 * (3 * (2 * fact(1))))
# ||||| 5 * (4 * (3 * (2 * (1 * fact(0)))))
# |||||| 5 * 4 * 3 * 2 * 1 * 1
# 120
