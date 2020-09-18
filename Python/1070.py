
# 문제
# 월이 입력될 때 계절 이름이 출력되도록 해보자.

# 입력
# 월을 의미하는 1개의 정수가 입력된다.(1 ~ 12)

# 출력
# 계절 이름을 출력한다.


Month = input()
Month = int(Month)


if Month >= 3 and Month <= 5:
    print("spring")
elif Month >= 6 and Month <= 8:
    print("summer")
elif Month >= 9 and Month <= 11:
    print("fall")
else:
    print("winter")
