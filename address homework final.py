import json

addressbook = dict()

try:
    with open("addressbook.json", "r", encoding="utf-8") as f:
        addressbook = json.load(f)
except:
    print("오류")

name = None
while(True) :
    name = input('이름을 입력하세요: ')
    if(name == '끝'):
        break

    if name in addressbook:
        print('이미 주소록에 있는 이름입니다.')
        continue
    
    phoneNum = input('전화번호를 입력하세요: ')
    addressbook[name] = phoneNum

print('주소록이 저장되었습니다.')

while True:
    delete_name = input('삭제할 이름을 입력하세요: ')
    
    if delete_name == '끝':
        break
    if delete_name in addressbook:
        addressbook.pop(delete_name)
        print(delete_name, '삭제완료')
    else:
        print('이 이름은 주소록에 없습니다.')

with open("addressbook.json", "w", encoding="utf-8") as f:
    json.dump(addressbook, f, ensure_ascii=False, indent=4)

print("주소록이 저장되었습니다.")

print("불러온 주소록:", addressbook)
print("불러온 주소록:")
for name in addressbook:
    print(name, ":", addressbook[name])
