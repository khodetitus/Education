# eval
# example 1
say_hello = 'print("hello")'
eval(say_hello)
# example 2
say_hello = 'print(name)'
eval(say_hello, {"name": "MasouD"})

# exec
# example 1
name = 'name="masoud"\nprint(name)'
exec(name)
# example 2
say_hello = '''
def show(name):
    print(f"hello {name}")
show(my_name)    
'''
exec(say_hello, {"my_name": "masoud"})

