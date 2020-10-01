
# 문제
# 정보 선생님은 수업을 시작하기 전에 이상한 출석을 부른다.
# 학생들의 얼굴과 이름을 빨리 익히기 위해 번호를 무작위(랜덤)으로 부르는데,
# 영일이는 선생님이 부른 번호들을 기억하고 있다가 거꾸로 불러보는 것을 해보고 싶어졌다.
# 출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력해 보자.

# 입력
# 번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
# n개의 랜덤 번호(k, 1 ~ 23)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.

# 출력
# 출석을 부른 번호 순서를 바꾸어 공백을 두고 출력한다.

n = int(input())
a = []
a = input().split()

while n != 0:
    print(a[n-1], end=' ')
    n = n - 1