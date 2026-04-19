# lab 7-1
import datetime

now = datetime.datetime.now()
print('{}년 {}월 {}일'.format(now.year, now.month, now.day))

hour = now.hour

if hour < 12 :
    time = '오전'
    time_hour = hour

else :
    time = '오후'
    time_hour = hour - 12
    
print('{} {}시 {}분 {}초'.format(time, time_hour, now.minute, now.second))
