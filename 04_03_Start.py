# Calendar Module
from datetime import datetime, timedelta
import calendar

now = datetime.now()

testDate = now + timedelta(days=2)
myFirstLinkedInCourse = now - timedelta(weeks=3)

print(now.date())
print(testDate.date())
print(myFirstLinkedInCourse.date())

if testDate > myFirstLinkedInCourse:
    print('Comparison works')

cal = calendar.month(2018, 8)
print(cal)

cal2 = calendar.weekday(2018, 8, 9)
print(cal2)

print(calendar.isleap(2018))
print(calendar.isleap(2020))
