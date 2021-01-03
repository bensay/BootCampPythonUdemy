import datetime

# print date of now as the following format DayName Day MonthName Year
x = datetime.datetime.now()
print(x.strftime('%A %dd %B %Y'))
