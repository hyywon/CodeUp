
# 문제
# 영문자 1개를 입력받아 그 다음 문자를 출력해보자.
# 영문자 'A'의 다음 문자는 'B'이고, 영문자 '0'의 다음 문자는 '1'이다.

# 입력
# 영문자 1개가 입력된다.

# 출력
# 다음 문자를 출력한다.

a = input()
a = ord(a)
a = a+1

print(chr(a))