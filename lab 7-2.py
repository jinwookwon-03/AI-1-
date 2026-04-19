# lab 7-2 / 1
import datetime as dt
today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
xMas = dt.datetime(2026, 12, 25)
time_gap = xMas - dt.datetime.now()
print('2026년 크리스마스 까지는 {}일 {}시간 남았습니다.'.format(\
time_gap.days, time_gap.seconds // 3600))

# lab 7-2 / 2
import datetime as dt
today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
year_2036 = dt.datetime(2036, 1, 1)
time_gap = year_2036 - dt.datetime.now()
print('2036년 새해 까지는 {}일 {}시간 남았습니다.'.format(\
time_gap.days, time_gap.seconds // 3600))

# lab 7-2 / 3
import datetime as dt
today = dt.date.today()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
birthday = dt.datetime(2026, 8, 20)
time_gap = birthday - dt.datetime.now()
print('2026년 생일까지는 {}일 {}시간 남았습니다.'.format(\
time_gap.days, time_gap.seconds // 3600))
