# lab 7-5 / 1
import random as rd

num1 = rd.randrange(0, 101, 5)
num2 = rd.randrange(0, 101, 5)
num3 = rd.randrange(0, 101, 5)
numlist = [num1, num2, num3]

print('0에서 100이하의 정수 중에서 5의 배수' , numlist)

# lab 7-5 / 1
import random as rd

numlist = []
for i in range(1, 11 ,1):
    numlist.append(i)
result = rd.sample(numlist,3)
print('1에서 10 사이의 임의의 정수 :' , result)
