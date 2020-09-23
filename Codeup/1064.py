
# 문제
# 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
# 단, 조건문을 사용하지 않고 3항 연산자 ? 를 사용한다.

# 입력
# 3개의 정수가 공백으로 구분되어 입력된다.
# -2147483648 ~ +2147483648

# 출력
# 가장 작은 값을 출력한다.

A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

res = A if A<B else B
res = res if res<C else C
print(res)