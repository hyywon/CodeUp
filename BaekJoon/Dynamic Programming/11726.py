# 문제
# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
# 아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.


# 입력
# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

# 출력
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

# 2*2 = 2-2 + 2-1  = 2 
# 2*3 = 3-2 + 3-1 = 3
# 2*4 = 4-2 + 4-1 = 5
# 2*5 = 5-2 + 5-1 = 8

import sys
read = sys.stdin.readline
n = int(read())
# 2*0 , 2*1, 2*2 일 때
tile = [0, 1, 2]

for a in range(3, n+1):
    tile.append(tile[a-1] + tile[a-2])

print(tile[n] % 10007)