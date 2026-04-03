i = 0
while i < 5:
    print('Welcome to everyone!!')
    i += 1

for i in range(0, 5, 1):
    print('Welcome to everyone!!')

#같은식

isum = 0
n_list = [0, 2, 5, 10]
for i in n_list:
    isum += i

print(isum)
#같은식
n_list = [0, 2, 5, 10]
isum = 0
i = 0
while i < 4: 
    isum += n_list[i]
    i += 1


print(isum)

#list의 개수 4개 미만 but
#이렇게 하면 list의 개수를 알아야함
#=> while i<len(n_list):
