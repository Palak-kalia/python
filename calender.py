import calendar
yy=2024
mm=3
# print(calendar.calendar(yy))

# import datetime
# time=datetime.datetime.now()
# print(time.year)
# print(time.month)
# print(time.day)
# print(time.hour)

import time
time=time.strftime("%H:%M:%S",time.localtime())
print(time)



