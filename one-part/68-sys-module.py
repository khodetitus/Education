import sys

# directory python:
print(sys.path)
sys.path.append("/home")
print(sys.path)
# The largest integer that can be stored in RAM:
print(sys.maxsize)
# show the executable python in system:
print(sys.executable)
# display os type:
print(sys.platform)
# show the active version python in system:
print(sys.version)
# Exiting the program from execution mode:
if sys.platform == "linux":
    exit()
elif sys.platform == "windows":
    print("this system platform is windows")
