# 문제
# N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.
# P1 IOI
# P2 IOIOI
# P3 IOIOIOI
# PN IOIOI...OI (O가 N개)
# I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. 둘째 줄에는 S의 길이 M이 주어지며, 셋째 줄에 S가 주어진다. (1 ≤ N ≤ 1,000,000, 2N+1 ≤ M ≤ 1,000,000)

# 출력
# S에 PN이 몇 군데 포함되어 있는지 출력한다.

import sys 
read = sys.stdin.readline

N = int(read())
length = int(read())
IOIO = read().rstrip()
count = 0
pn = 0
l = 1

while l < length-1: 
    if IOIO[l] == 'O' and IOIO[l-1] == 'I' and IOIO[l+1] == 'I':
        # IOI 패턴이 N개 연속적으로 있으면 PN 이 됨 
        # PN 패턴 체크를 하기위해서 IOI 하나 만나면 pn + 1 해 준다.
        pn += 1
        # pn 이 N 과 같다면 패턴을 찾은 것이기 때문에 pn을 하나 감소(뒤 문자열에서 IOI )
        if pn == N:
            # 바로 뒤에 IOI 패턴이 있으면 패턴을 하나 더 찾게 되는 것 
            # pn을 -1 해줌
            pn -= 1 
            count += 1
        # O를 기준으로 문자열 검색을 했기 때문에 바로 다음의 I를 건너띄고 다음 문자열로 확인하기 위해 +1 
        l += 1

    # IOI를 찾더라도 pn이 N에 맞지 않다면 패턴이 아니기 때문에 pn 초기화
    # IOI를 못 찾았다면 pn 초기화
    else:
        pn = 0
    l += 1


print(count)