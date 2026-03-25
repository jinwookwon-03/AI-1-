#lab 3-3 / 1
score = int(input("게임점수를 입력하시오 : "))
print("game_score = ", score)
if score >= 1000 :
    print("고수입니다.")
else :
    print("입문자입니다.")


#lab 3-3 / 2
a = int(input("한 정수를 입력하시오 : "))
b = int(input("다른 정수를 입력하시오 : "))
if a == b :
    print("두 값이 일치합니다.")
else :
    print("두 값이 일치하지 않습니다.")

#lab 3-3 / 3
age = int(input("당신은 성인인가요(성인이면1, 미성년이면 0): "))
if age == 0 :
    print("당신은 미성년자입니다.")
elif age == 1 :
    marry = int(input("결혼을 하셨나요(기혼이면 1, 미혼이면 0): "))
    if marry == 1 :
        print("당신은 결혼한 성인입니다.")
    else :
        print("당신은 결혼하지 않은 성인입니다.")
    
