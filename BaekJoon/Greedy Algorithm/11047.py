# 문제
# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
# 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다.
#  (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

# 출력
# 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출10 
n, sum = map(int,input().split())
won = []
res = 0

for _ in range(0, n):
    won.append(int(input()))

# 동전 단위 큰 순서로 정렬
won.sort(reverse=True)

for i in range(0, n):
    # 남은 합이 동전보다 크거나 같을 경우
    if sum >= won[i]:
        # 합을 동전으로 나눈 몫 만큼 사용
        res += sum // won[i]
        sum -= (sum // won[i]) * won[i]
    else:
        pass


print(res)
