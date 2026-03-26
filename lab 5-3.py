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
