# lab 5-5 / 1-(1)
a = [1, 2, 3]
b = [10, 20, 30]
a.append(b)
print(a)

# lab 5-5 / 1-(1)
a = [1, 2, 3]
b = [10, 20, 30]
a.extend(b)
print(a)

# lab 5-5 / 2
nlist = []
for i in range(1, 11, 1):
    nlist.append(i)
print('nlist = ', nlist)

# lab 5-5 / 3
nlist = []
for i in range(1, 11, 1):
    nlist.append(i)
nlist.insert(0, 0)
print('nlist = ', nlist)

# lab 5-5 / 4
nlist = []
for i in range(1, 11, 1):
    nlist.append(i)
nlist.insert(0, 0)
nlist.reverse()
print('nlist = ', nlist)

# lab 5-5 / 5
nlist = []
for i in range(1, 11, 1):
    nlist.append(i)
nlist.insert(0, 0)
nlist.reverse()
print('마지막 원소 =', nlist.pop())
print('nlist = ', nlist)
