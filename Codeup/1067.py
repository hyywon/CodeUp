
# 문제
# 정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.

# 입력
# 정수 1개가 입력된다.
# -2147483648 ~ +2147483647, 단 0은 입력되지 않는다.

# 출력
# 입력된 정수에 대해
# 첫 줄에 minus 나 plus 를 출력하고,
# 두 번째 줄에 odd 나 even 을 출력한다.

A = input()
A = int(A)

if A > 0:
    print("plus")
else:
    print("minus")

if A%2 is 0:
    print("even")
else:
    print("odd")