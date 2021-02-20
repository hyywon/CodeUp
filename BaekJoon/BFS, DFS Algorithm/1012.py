# 문제
# 차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다. 
# 농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에, 
# 한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다. 
# 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 
# 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 
# 그 배추들 역시 해충으로부터 보호받을 수 있다.
# (한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있다고 간주한다)
# 한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어놓았다. 
# 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 
# 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다.
# 예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다.
# (0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.)

# 1  1	0	0	0	0	0	0	0	0
# 0	 1	0	0	0	0	0	0	0	0
# 0	 0	0	0	1	0	0	0	0	0
# 0	 0	0	0	1	0	0	0	0	0
# 0	 0	1	1	0	0	0	1	1	1
# 0	 0	0	0	1	0	0	1	1	1

# 입력
# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 
# 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다.

# 출력
# 각 테스트 케이스에 대해 필요한 최소의 배추흰지렁이 마리 수를 출력한다.

import sys
read = sys.stdin.readline
from collections import deque

# dfs 시간초과 검색하니까 뜸 재귀 시간초과 때문에 ,, ,, ,,
sys.setrecursionlimit(10 ** 6)

# 우, 하, 좌 , 상
# (1,0) (0,-1) (-1,0) (0,1)
dx = [0,1,0,-1]
dy = [1,0,-1,0]

vis = []
t = int(read())



def bfs(x,y):
    # 배추벌레가 있기 때문에 dfs가 실행됨 , vis에 기록
    vis[x][y] = 1
    chk = deque()
    chk.append((x,y))
    while chk:
        x,y = chk.popleft()
        for i in range(4):
            fx = x + dx[i]
            fy = y + dy[i]

            if 0 <= fx and fx < n and 0 <= fy and fy < m:
                # 배추 벌레가 있고, 방문하지 않았을 경우에만 dfs 실행
                if mat[fx][fy] == 1 and vis[fx][fy] == 0:
                    chk.append((fx,fy))
                    bfs(fx,fy)


def dfs(x,y):
    print(x,end=",")
    print(y)
    global cnt
    vis[x][y] = 1
    for i in range(4):
        fx = x + dx[i]
        fy = y + dy[i]    

        if 0 <= fx and fx < n and 0 <= fy and fy < m:
            # 배추 벌레가 있고, 방문하지 않았을 경우에만 dfs 실행
            if mat[fx][fy] == 1 and vis[fx][fy] == 0:
                dfs(fx,fy)


for _ in range(t):
    m,n,k = map(int, read().split())
    mat = [[0] * m for _ in range(n)]
    vis = [[0] * m for _ in range(n)]
    cnt = 0

    # 행렬 생성
    for _ in range(k):
        q,w = map(int, read().split())
        mat[w][q] = 1

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1 and vis[i][j] == 0:
                bfs(i,j)
                cnt += 1
    print(cnt)

