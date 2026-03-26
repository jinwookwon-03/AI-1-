# lab 5-1 / 1
even_list = [2, 4, 6, 8, 10]
print("even_list =", even_list)

# lab 5-1 / 2
even_list = list(range(2, 11, 2))
print("even_list =", even_list)

# lab 5-1 / 3
nations = ['Korea', 'China', 'India', 'Nepal']
print('nations = ' , nations)

# lab 5-1 / 4
friends = ['길동', '철수', '은지', '지은', '영민']
print('friends = ' , friends)

# lab 5-1 / 5
string = list('XYZ')
print('string = ', string)

# lab 5-2 / 1
prime_list = [2, 3, 5, 7]
print('prime_list의 첫 원소 :', prime_list[0])

# lab 5-2 / 2
prime_list = [2, 3, 5, 7]
print('prime_list의 마지막 원소 :', prime_list[3])

# lab 5-2 / 3
prime_list = [2, 3, 5, 7]
print('prime_list의 마지막 원소 :', prime_list[-1])

# lab 5-2 / 4
nations = ['Korea', 'China', 'Russia', 'Malaysia']
print('nations의 첫 원소 :', nations[0])

# lab 5-2 / 5
nations = ['Korea', 'China', 'Russia', 'Malaysia']
print('nations의 마지막 원소 :', nations[-1])

# lab 5-2 / 6
nations = ['Korea', 'China', 'Russia', 'Malaysia']
print('nations의 마지막 원소 :', nations[len(nations)-1])


# lab 5-3 / 1
prime_list = [2, 3, 5, 7]
print('소수 목록 :', prime_list)
prime_list.append(11)
print('추가 후 소수 목록 :', prime_list)

# lab 5-3 / 2
prime_list = [2, 3, 5, 7]
prime_list.append(11)
print('삭제 전 소수 목록 :', prime_list)
prime_list.remove(3)
print('삭제 후 소수 목록 :', prime_list)

# lab 5-3 / 3
nations = ['Korea', 'China', 'Russia', 'Malaysia']
print('국가 목록 :', nations)
nations.append('Nepal')
print('추가 후 국가 목록 :', nations)

# lab 5-3 / 4
nations = ['Korea', 'China', 'Russia', 'Malaysia']
nations.append('Nepal')
if ('Japan' in nations) :
    print('Japan 는(은) 국가 목록에 있습니다.')
else :
    print('Japan 는(은) 국가 목록에 없습니다.')
if ('Russia' in nations) :
    print('Russia 는(은) 국가 목록에 있습니다.')
else :
    print('Russia 는(은) 국가 목록에 없습니다.')

# lab 5-4 /1
prime_list = [2, 3, 5, 7]
print('1에서 10까지의 소수 :', prime_list)
print('최솟값 :' ,min(prime_list))
print('최댓값 :' ,max(prime_list))
print('합계 :' ,sum(prime_list))
print('평균 :' ,sum(prime_list)/len(prime_list))

# lab 5-4 / 2
nations = ['Korea', 'China', 'Russia', 'Malaysia']
print('국가 목록 :', nations)
print('사전에 가장 먼저 나오는 나라 :', min(nations))
print('사전에 가장 뒤에 나오는 나라 :', max(nations))

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

# lab 5-6 / 1
list = [1, 2, 3]
n = int(input('반복할 정수를 입력하시오 :'))
print(n * list)

# lab 5-7 / 1
n_list = list(range(15))
print('n_list =', n_list)
    
# lab 5-7 / 2
n_list = list(range(5))
print('s_list1 =', n_list)

n_list = list(range(5, 11, 1))
print('s_list2 =', n_list)    

n_list = list(range(11, 15, 1))
print('s_list3 =', n_list)

n_list = list(range(2, 11, 2))
print('s_list4 =', n_list) 

n_list = list(range(10, 5, -1))
print('s_list5 =', n_list)

n_list = list(range(10, 1, -2))
print('s_list6 =', n_list) 
