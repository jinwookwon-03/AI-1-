#lab 8-3 / 1
a = [1, 2, 3, 4, 5]
choice = int(input('a의 요소를 하나 선택하시오: '))
if choice in a:
    if choice == 1:
        print('{}은(는) 첫 번째 요소입니다'.format(choice))
    elif choice == 2:
        print('{}은(는) 두 번째 요소입니다'.format(choice))
    elif choice == 3:
        print('{}은(는) 세 번째 요소입니다'.format(choice))
    elif choice == 4:
        print('{}은(는) 네 번째 요소입니다'.format(choice))
    elif choice == 5:
        print('{}은(는) 다섯 번째 요소입니다'.format(choice))

#lab 8-3 / 2
try:
    a = [1, 2, 3, 4, 5]
    choice = int(input('a의 요소를 하나 선택하시오: '))
    if choice in a:
        if choice == 1:
            print('{}은(는) 첫 번째 요소입니다'.format(choice))
        elif choice == 2:
            print('{}은(는) 두 번째 요소입니다'.format(choice))
        elif choice == 3:
            print('{}은(는) 세 번째 요소입니다'.format(choice))
        elif choice == 4:
            print('{}은(는) 네 번째 요소입니다'.format(choice))
        elif choice == 5:
            print('{}은(는) 다섯 번째 요소입니다'.format(choice))
except ValueError:
    print('오류 : 입력 값이 정수나 실수가 아님')


