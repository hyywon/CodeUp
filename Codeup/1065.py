
# 문제
# 세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.

# 입력
# 세 정수 a, b, c 가 공백을 두고 입력된다.
# 0 ~ +2147483647 범위의 정수들이 입력되며 적어도 1개는 짝수이다.

# 출력
# 짝수만 순서대로 줄을 바꿔 출력한다.

A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

even = []

if A%2 is 0:
    even.append(A)
if B%2 is 0:
    even.append(B)
if C%2 is 0:
    even.append(C)

for item in even:
    print(item)