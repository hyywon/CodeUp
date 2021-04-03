# 문제
# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 
# 단, 모든 간선의 가중치는 10 이하의 자연수이다.

# 입력
# 첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1≤V≤20,000, 1≤E≤300,000) 
# 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 
# 둘째 줄에는 시작 정점의 번호 K(1≤K≤V)가 주어진다. 
# 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 
# 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 
# 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

# 출력
# 첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 
# 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.

import sys, heapq
read = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, read().split())
k = int(sys.stdin.readline())
graph = [[] for _ in range(v + 1)]
cost = [INF] * (v + 1)
heap = []

def dijkstra(start):
    # 시작 node에 대해 초기화
    cost[start] = 0 # start에서 start로 거리 0으로 초기 설정
    heapq.heappush(heap, [0, start])

    while heap:
        # 거리가 제일 작은 node 선택
        # 현재까지의 거리, 지금 위치한 곳의 정점
        weight, node = heapq.heappop(heap)

        if cost[node] < weight:
            # 최소 거리일때만 실행
            continue

        # 현재 node와 연결된 다른 node를 확인
        for cur_node, cur_weight in graph[node]:
            n_weight = cur_weight + weight # 해당 node를 거쳐 갈 때 거리 
            if n_weight < cost[cur_node]: # 현재 거리보다 작으면 갱신
                cost[cur_node] = n_weight
                heapq.heappush(heap, [n_weight, cur_node]) # 다음 인접 node를 계산하기 위해 heap 에 삽입

# graph 생성
for i in range(e):
    u, v, w = map(int, read().split())
    graph[u].append([v, w])

dijkstra(k)

for i in cost[1:]:
    print(i if i != INF else "INF")