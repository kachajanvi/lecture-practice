#(1)date time module
#importing datetime module
import datetime
now = datetime.datetime.now()
print(now)

#current dateonly
today = datetime.date.today()
print(today)

#custom date
custom = datetime.date(2024,12,24)
print(custom)

#access year,month,day
today = datetime.date.today()
print("year:",today.year)
print("month:",today.month)
print("day:",today.day)

#strtime() is used to format date and time
now = datetime.datetime.now()
formatted = now.strftime("%d - %m - %Y %H: %M: %S:")
print(formatted)

#date difference
d1 = datetime.date(2002,12,1)
d2 = datetime.date(2026,6,11)

difference = d2-d1
print(difference.days)

#(2)time module in python
#import time module
import time
current = time.time()
print(current)

#pause program using sleep()
print("start")
time.sleep(3)
print("end after 3 seconds")

#current local time
local = time.localtime()
print(local)

#format time
current = time.strftime("%H: %M: %S")
print(current)

#measure execution time
start = time.time()
for i in range(1000000):
    pass
end = time.time()
print("execution time:",end-start)


#(1).display current date and time
from datetime import datetime

now = datetime.now()

print(now)
print("year:",now.year)
print("month:",now.month)
print("day:",now.day)
print("hour:",now.hour)
print("second:",now.second)

#datetime.datetime.utcnow()
#return current UTC now
import datetime
print(datetime.datetime.utcnow())

#srtptime()
#converts  string into datetime object

from datetime import datetime
date = "2025-06-11"
obj = datetime.strptime(date,"%Y-%m-%d")
print(obj)

#timedelta
#used to date calculation

from datetime import datetime,timedelta
today = datetime.now()
future = today + timedelta(days=5)
print(future)

#replace()
#Replace year\month\day etc....
now = datetime.now()
new_date = now.replace(month=2)
print(new_date)

#weekday()
#return weekday number

now = datetime.now()
print(now.weekday())

#isoweekday()
#return readable weekdays number(1-7)
now = datetime.now()
print(now.isoweekday())

#ctime
#return readable date and time

now = datetime.now()
print(now.ctime())

#timestamp()
#return second since epoch

now = datetime.now()
print(now.timestamp())

#from timestamp()
#converts time stamp to datetime

s =174983000
print(datetime.fromtimestamp(s))

#python time module method
#returns UTC time object
import time
print(time.gmtime())

#mktimk()
import time
t = time.localtime()
print(time.mktime(t))

#asctime()
import time
t = time.localtime()
print(time.asctime(t))

#monotonic()
import time
print(time.monotonic())
