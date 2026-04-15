#Lab 6-7 / 1
person = (2019001, '홍길동', 179)
print('person =', person)

#Lab 6-7 / 2
person = (2019001, '홍길동', 179)
person[0] = 2019003
print(person)

#Lab 6-7 / 3
person = (2019001, '홍길동', 179)
person = list(person)
person[0] = 2019003
person = tuple(person)
print('person =', person)
