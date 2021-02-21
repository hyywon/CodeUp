# 문제
# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
#  철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
#  여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
#  대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
#  지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.



# 입력
# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
#  그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

# 출력
# 첫 번째 줄에는 총 단지수를 출력하시오. 
# 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

import sys
read = sys.stdin.readline
from _collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]
vis = []
mat = []
t = int(read())
cnt = 0
res = []


def bfs(x,y):
    global cnt, count
    # 집이  있기 때문에 bfs가 실행됨 , vis에 기록하고 집 갯수 +1
    chk = deque()
    chk.append((x,y))
    vis[x][y] = 1
    count += 1

    while chk:
        x,y = chk.popleft()
        for i in range(4):
            fx = x + dx[i]
            fy = y + dy[i]

            if 0 <= fx and fx < t and 0 <= fy and fy < t:
                # 집이 있고, vis에 기록하지 않았을 경우에만 dfs 실행
                if mat[fx][fy] == 1 and vis[fx][fy] != 1:
                    chk.append((fx,fy))
                    bfs(fx,fy)


def dfs(x,y):
    global cnt, count
    # 집이  있기 때문에 dfs가 실행됨 , vis에 기록하고 집 갯수 +1
    vis[x][y] = 1
    count += 1

    for i in range(4):
        fx = x + dx[i]
        fy = y + dy[i]

        if 0 <= fx and fx < t and 0 <= fy and fy < t:
            # 집이 있고, vis에 기록하지 않았을 경우에만 dfs 실행
            if mat[fx][fy] == 1 and vis[fx][fy] != 1:
                bfs(fx,fy)


for _ in range(t):
    # '\n' 전까지 list로 입력
    mat.append(list(map(int,read()[:-1])))


vis = [[0] * t for _ in range(t)]
for i in range(t):
    for j in range(t):
         
        # 집이 있고, vis에 기록하지 않았을 경우에만 dfs 실행
        if mat[i][j] == 1 and vis[i][j] == 0:
            # 한 단지가 끝나고나면 집 갯수 초기화
            count = 0
            dfs(i,j)
            # 모든 단지를 dfs 하고 난 후, 집 갯수 res 에 추가
            res.append(count)
            # 단지 갯수 증가
            cnt += 1
            
print(cnt)
res.sort()
for i in res:
    print(i)
