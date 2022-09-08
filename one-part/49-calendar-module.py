import calendar as cr

# 1.month method
print(cr.month(1997, 7))

# 2.calendar method
print(cr.calendar(1997))

# 3. isleap method
print(cr.isleap(2016))

# 4.leapdays method
print(cr.leapdays(1997, 2022))

# 5.monthcalendar method
print(cr.monthcalendar(1997, 7))

# 6.monthname method
for name_month in cr.month_name:
    print(name_month)

# 7.itermonthdates method
month_generator = cr.Calendar()
for name_month in month_generator.itermonthdates(1997, 7):
    print(name_month)

# 9.formatmonth method
html_instance = cr.HTMLCalendar()
print(html_instance.formatmonth(1997, 7))
