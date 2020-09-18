
# 문제
# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

# 입력
# 정수 1개가 입력된다.
# (0 ~ 100)

# 출력
# 1부터 입력된 수까지 짝수의 합을 출력한다.

A = input()
A = int(A)
num = []
i = 0
sum = 0

while i <= A:
    if i%2 == 0:
        num.append(i)
    i = i + 1

for item in num:
    sum = sum + item

print(sum)