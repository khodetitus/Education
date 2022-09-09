import datetime as dt
import pytz as tz

# 1.date
# example 1
date = dt.date(1997, 9, 7)
print(date)
print(date.year)
print(date.month)
print(date.day)

# example 2
# date.fromtimestamp()
print(dt.date.fromtimestamp(786384))  # 1997-01-01 00:00:00 #input: second ,output:date in elapsed seconds

# example 3
# date.today()
print(dt.date.today())

# 2.time
time = dt.time(4, 32, 15, 10)
print(time)
print(time.hour)
print(time.minute)
print(time.second)
print(time.microsecond)

# 3.datetime
# example 1
date_time = dt.datetime(1997, 11, 23, hour=4, minute=32, second=15, microsecond=10)
print(date_time)

# example 2
# datetime.now()
print(dt.datetime.now())

# example 3
# datetime.timestamp()
date_time = dt.datetime(1997, 11, 23, hour=4, minute=32, second=15, microsecond=10)
print(date_time.timestamp())
# example 4
# dt.datetime.strptime()
date_string = "1997-07-09 12:30:07"
convert_date = dt.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(convert_date)
# see the all formats in strptime:

# %a:  abbreviated weekday as Sun, Mon
# %A:  weekdays full name
# %w:  weekdays as number
# # %d:  days in number and zero-padded 01, 02
# %b:  Months abbreviate as Apr, Jun
# %B:  Months full name April, June
# %m:  months in number and zero-padded 03, 06
# %y:   Year without century 21, 20, 19
# %Y:  Year with century 2021, 2020, 2019
# %H:  24 hours clock 00 - 23 zero-padded
# %I:   12 hours clock 01 - 12 zero-padded
# %p:   Period of the day as AM/PM
# %M:  Minutes from 00 - 59 zero-padded
# %s:   seconds from 00 - 59 zero-padded
# %f:    microseconds 6 decimal places

# example 5
# dt.datetime.strftime()
date_time = dt.datetime.today()
convert_date = dt.datetime.strftime(date_time, "%Y-%m-%d %H:%M:%S")
print(convert_date)
print(type(convert_date))

# 4.timedelta
# example 1
date1 = dt.date(1997, 9, 9)
date2 = dt.date.today()
print(date2 - date1)

# example 2
# dt.timedelta()
date_now = dt.date.today()
date_choose = dt.timedelta(weeks=14, days=5)
print(date_now + date_choose)
# 6.timezone
local = dt.datetime.now()
new_york = dt.datetime.now(tz.timezone("America/new_york"))
print(local)
print(new_york)

# see the all timezones in pytz with using all_timezones
for country_city in tz.all_timezones:
    print(country_city)
