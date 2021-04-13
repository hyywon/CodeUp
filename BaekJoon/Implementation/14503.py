# 방향 이동, 북 동 남 서
x = [-1,0,1,0]
y = [0,1,0,-1]
 
N,M = map(int,input().split())
r,c,dir = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
 
cleaned = [[0]*M for _ in range(N)]

res = 1
cleaned[r][c] = 1
 
temp = []
temp.append([r,c])
 
while len(temp) != 0:
 
    i,j = temp.pop(0)
 
    for q in range(4):
 
        # 현재 바라보는 방향 기준에서 왼쪽 확인하기
        N_i = i + x[(dir + 3 - q) % 4]
        N_j = j + y[(dir + 3 - q) % 4]
 
        # 빈칸이고, 청소 안 한 곳이면
        if board[N_i][N_j] == 0 and cleaned[N_i][N_j] == 0:
 
            # 위치 값 추가
            temp.append([N_i,N_j])
 
            # 청소 확인
            cleaned[N_i][N_j] = 1
 
            # 청소한 영역 +1
            res += 1
 
            # 바라보는 방향 바꾸기
            dir = (dir + 3 - q) % 4
 
            # 일단 찾아서 이동하면 더 이상 돌아볼 필요 없음
            break
 
    # 다 돌았는데 이동 못한 경우에는 temp가 비어있음
    if len(temp) == 0:
 
        # 현재 방향에서 후진하기
        N_i = i+x[(dir+2)%4]
        N_j = j+y[(dir+2)%4]
 
        # 빈칸이면 temp 값 추가
        if board[N_i][N_j] == 0:
            temp.append([N_i, N_j])
 
print(res)