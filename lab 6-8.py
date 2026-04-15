#Lab 6-8 / 1
def square(a, b):
    return a**2, b**2

x = int(input('x ='))
y = int(input('y ='))
x_sq, y_sq = square(x, y)
print('{} 제곱 = {}, {} 제곱 = {}'.format(x, x_sq, y, y_sq))

#Lab 6-8 / 2
t1 = (10, 20, 30)
t2 = (40, 50, 60)
print(t1 + t2)

#Lab 6-8 / 3
print('Hello ' * 3)
print(('Hello ',) * 3)
