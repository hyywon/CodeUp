# 문제
# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다.
# O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.
# 예를 들어, 10번 문제의 점수는 3이 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다.
# 문자열은 O와 X만으로 이루어져 있다.

# 출력
# 각 테스트 케이스마다 점수를 출력한다.


n = int(input())
ox = []

for i in range(n):
    # 입력되는 문자열 '\n'를 제거하고 list에 추가 
    ox.append((input()).rstrip())

for j in ox:
    score = 0
    cnt = 0
    # O일 경우 cnt 값 + 1, cnt를 이용해서 X를 만나기전 까지 cnt를 증가
    # 증가되는 cnt를 더해서 score 기록
    for i in j:
        if i == 'O':
            cnt += 1
            score += cnt
        # X일 경우 cnt 를 0으로 초기화 
        elif i == 'X':
            cnt = 0
            score += cnt
    print(score)

