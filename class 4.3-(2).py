'''
selected = None
while selected not in ['가위', '바위', '보']:
    selected = input('가위, 바위, 보 중에서 선택하세요')
print('선택한 값은:', selected)

st = 'Programming'
for ch in st:
    if ch in ['a', 'e', 'i', 'o', 'u']:
        continue
    print(ch)
print('The end')

st = 'Programming'
for ch in st:
    if ch in ['a', 'e', 'i', 'o', 'u']:
        break
    print(ch)
print('The end')
