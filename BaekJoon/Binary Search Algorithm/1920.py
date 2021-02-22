# 문제
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 
# 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 
# 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 
# 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

# 출력
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

import sys
read = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(read())
A = list(map(int,read().split()))
m = int(read())
B = list(map(int, read().split()))

A.sort()

# 이진 탐색, 재귀 형식 (중앙)
# 메모리 초과 → search에 전부 전달 해줘야 함
def search(x,low, high,data):  
    if low > high:
        return False
    mid = (low+high) // 2
    if data[mid] == x:
        return True
    # 찾는 값 보다 중앙 값이 크다면 절반의 앞쪽에서 탐색
    elif data[mid] > x:
        return search(x,low,mid-1,data)
    # 찾는 값 보다 중앙 값이 작다면 절반의 뒤쪽에서 탐색
    elif data[mid] < x:
        return search(x,mid+1,high,data)


for i in B:   
    if search(i,0,n-1,A):
        print(1)
    else: 
        print(0)
