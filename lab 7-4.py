# lab 7-4 / 1
import math as m

for i in range(2, 11, 1):
    result = m.pow(4, i)
    print('{}** {} = {}'.format(4, i, result))
          
# lab 7-4 / 2
import math as m
for i in range(0, 181, 10):
    result = m.radians(i)
    print('{} degree = {} radian'.format(i, round(result,3)))

# lab 7-4 / 3
import math as m
for i in range(0, 181, 10):
    result = m.sin(m.radians(i))
    print('sin({}) = {}'.format(i, round(result,2)))
