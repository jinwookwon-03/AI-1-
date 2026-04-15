#Lab 6-5 / 1
fruits_dic = {'apple' : 6000, 'melon' : 3000, 'banana' : 5000, 'orange' : 4000}
keys_list = list(fruits_dic.keys())
print(list)

#Lab 6-5 / 2
fruits_dic = {'apple' : 6000, 'melon' : 3000, 'banana' : 5000, 'orange' : 4000}
values_list = list(fruits_dic.values())
print(list)

#Lab 6-5 / 3
fruits_dic = {'apple' : 6000, 'melon' : 3000, 'banana' : 5000, 'orange' : 4000}
print('fruits_dic 딕셔너리의 항목의 개수 :', len(fruits_dic))

#Lab 6-5 / 4
fruits_dic = {'apple' : 6000, 'melon' : 3000, 'banana' : 5000, 'orange' : 4000}
if 'apple' in fruits_dic.keys():
    print('apple is in fruits_dic.')
else:
    print('apple is not in fruits_dic.')
if 'mango' in fruits_dic.keys():
    print('mango is in fruits_dic.')
else:
    print('mango is not in fruits_dic.')
