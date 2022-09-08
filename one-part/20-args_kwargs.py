# normal arguments
def show(name):
    return f"hello {name}"


print(show("masoud"))
print(show("masoud", "kimiya", "saeid"))
print(show("masoud", "kimiya", "saeid", age=25, height=185))


# args and kwargs arguments
def show(name, *args, **kwargs):
    print(args)  # just for value and output:tuple   # print optional
    print(kwargs)  # for key and value and output:dictionary    # print optional
    return f"hello {name}"


print(show("masoud", "saeid", "kimiya", "hamide"))
print(show("masoud", "saeid", "kimiya", "hamide", age=25, height=185))
