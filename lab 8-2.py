#lab 8-2

#1
try:
    a = 10 * (30 / 0)
except ZeroDivisionError:
    print('0으로 나누는 오류')
except TypeError:
    print('지원되지 않은 연산자를 사용하는 오류')

#2
try:
    x = int(input('정수 x를 입력하세요: '))
except ValueError:
    print('오류 : 입력 값이 정수나 실수가 아닙니다')
except:
    print('정수나 실수를 입력하세요.')
else:
    print(x)
#3
import sys
try:
    f = open('myfile.txt')
    s = f.readline()
except FileNotFoundError:
    print('오류')

