import os

# see the methods and attribute in the os module
# print(dir(os))

# 1.uname method
# print(os.uname())

# 2.get working directory method
# print(os.getcwd())

# 3.list directory method
# print(os.listdir())
# print(os.listdir("/"))  # optional
# print(os.listdir("home"))  # optional

# 4.change directory method
# os.chdir("/")  # don't print just path to directory
# print(os.listdir())  # optional

# 5.make a directory method
# os.mkdir("first")  # don't print just path and name directory

# 6.remove a directory method
# os.rmdir("first")  # don't print just path and name directory

# 7.create nested directories method
# os.makedirs("first/second")

# 8.remove nested directories method
# os.removedirs("first/second")

# 9.show the environment method
# print(os.environ)

# 10.rename a directory method
# os.rename("first", "one")

# 11.access method:
# for To check the level of access to a file
file = os.listdir()[1]  # get the 1-lambda.py
print(os.access(file, os.R_OK))  # check the access of read file or no
