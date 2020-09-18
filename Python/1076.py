
# 문제
# 영문자(a ~ z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자.

# 입력
# 영문자 1개가 입력된다.(a ~ z)

# 출력
# a부터 입력한 문자까지 순서대로 공백을 두고 출력한다.

A = input()
res = (ord(A))
alpha = 97

while alpha <= res :
    print(chr(alpha))
    alpha = alpha + 1
