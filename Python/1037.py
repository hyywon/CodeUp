
# 문제
# 10진 정수 1개를 입력받아 아스키 문자로 출력해보자.
# 단, 0 ~ 255 범위의 정수만 입력된다.

# 입력
# 10진 정수 1개(0 ~ 255 범위)가 입력된다.

# 출력
# 아스키코드 값을 문자로 출력한다.

a = input()
a = int(a)

print(chr(a))