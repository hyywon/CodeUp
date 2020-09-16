
# 문제
# 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력해보자.
# 평가 내용
# 평가 : 내용
# A : best!!!
# B : good!!
# C : run!
# D : slowly~
# 나머지 문자들 : what?

# 입력
# 영문자 1개가 입력된다.
# (A, B, C, D 등의 한 문자가 입력된다.)

# 출력
# 평가내용에 따라 다른 내용이 출력된다.

A = input()

if A is "A":
    print("best!!!")
elif A is "B":
    print("good!!")
elif A is "C":
    print("run!")
elif A is "D":
    print("slowly~")
else:
    print("what?")


