import argparse

# example 1
parser = argparse.ArgumentParser()
parser.parse_args()
# run the terminal and enter using the code: python 154-argparse-module.py -h
# example 2
parser = argparse.ArgumentParser()
# parser.add_argument("name", help="please enter your name")  # name is a positional argument
# parser.add_argument("age", help="please enter your age", type=int)  # age a positional argument
parser.add_argument("-n", "--name", help="please enter your name")  # -n or --name is an optional argument
parser.add_argument("-a", "--age", help="please enter your age", type=int)  # -a or --age is an optional argument
parser.add_argument("-v", "--verbose", action="store_true")
args = parser.parse_args()
print(f"Hello {args.name}")
if args.verbose:
    print(f"Hello {args.name},you are {args.age} years old.")
# run positional argument:
# python 145-argument-module.py masoud 25
# run optional argument:
# python 145-argument-module.py -n or --name masoud -a or --age 25

# example 3
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="display a square of a given number")
parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
args = parser.parse_args()
short_answer = args.square ** 2
if args.verbose:
    print(f"the square of {args.square} equals {short_answer}")
else:
    print(short_answer)

# example 4
parser = argparse.ArgumentParser(description="this is a description", epilog="this is a epilog")
# parser.add_argument("--name", help="your name", action="store_const", const="masoud")
# parser.add_argument("--name", help="your name", action="const", const="masoud")
# parser.add_argument("--stat", help="your name", action="store_true")
# parser.add_argument("-n", "--numbers", action="append", type=int)
# parser.add_argument("-n", "--numbers", action="append_const", const=12)
# parser.add_argument("-n", "--numbers", action="count", default=12)
# parser.add_argument("-n", "--numbers", action="store", nargs="+", default=12)
parser.add_argument("-n", "--numbers", action="store", nargs=5)
args = parser.parse_args()
print(args)
