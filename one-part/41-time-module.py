import time as tm

# 1.gmtime method
print(tm.gmtime())
print(tm.gmtime(20000000))  # argument is optional

# 2.time method
print(tm.time())

# 3.ctime method
print(tm.ctime())

# 4.sleep method
print("Hello")
tm.sleep(4)  # dont print just enter the argument
print("World....")

# 5.strftime method
time = tm.ctime()
print(time)
convert_time = tm.strftime("%H:%M:%S %Y")
print(type(convert_time))
print(convert_time)

# 6. strptime method
time_string = "1997-07-09"
convert = tm.strptime(time_string, "%Y-%m-%d")
print(convert)

# 7.pref_counter method
# 8.process_time method
# example 1
per_start = tm.perf_counter()
prc_start = tm.process_time()

a = 0
for i in range(0, 100000000):
    a += 1

per_end = tm.perf_counter()
prc_end = tm.process_time()

print("performance counter -->", per_end - per_start)
print("process time -->", prc_end - prc_start)

# example 2
per_start = tm.perf_counter()
prc_start = tm.process_time()

tm.sleep(5)

per_end = tm.perf_counter()
prc_end = tm.process_time()

print("performance counter -->", per_end - per_start)
print("process time -->", prc_end - prc_start)

# 9.localtime method
local_time = tm.localtime()
print(local_time.tm_year)
print(local_time.tm_mon)

# 10.mktime method
mk_time = tm.localtime()
print(tm.mktime(mk_time))

# 11.asctime method
time = tm.localtime()
opt = tm.asctime(time)
print(f"Time Stamp is : {opt}")
