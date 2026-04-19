# lab 7-3 / 1
import datetime as dt
print('오늘 =', dt.datetime.now())
thousand = dt.timedelta(days = 1000)
plus1000day = dt.datetime.now() + thousand
print('1000일 후 =', plus1000day)

# lab 7-3 / 2
year, month, day = input('처음으로 사귄 연도와 월, 일을 입력하시오 :').split()
couple_day = dt.date(int(year), int(month), int(day))

hundred = dt.timedelta(days = 100)
plus100day = couple_day + hundred
print('100일 기념일은: {}년 {}월 {}일입니다.'.format(\
    plus100day.year, plus100day.month, plus100day.day))
