
# 문제
# 세 정수 a, b, c가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

# 입력
# 세 정수 a, b, c 가 공백을 두고 입력된다.
# 0 <= a, b, c <= +2147483647

# 출력
# 입력된 순서대로 짝(even)/홀(odd)을 줄을 바꿔 출력한다.

A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

if A%2 is 0:
    print("even")
else:
    print("odd")

if B%2 is 0:
    print("even")
else:
    print("odd")

if C%2 is 0:
    print("even")
else:
    print("odd")

