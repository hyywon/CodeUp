# 문제
# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

# 입력
# 첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.

# 출력
# 첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.

from itertools import permutations

n = int(input())
# 순열 사용하여 입력받은 모든 정수 값이 가질 수 있는 배열 생성
A = permutations(list(map(int,input().split())))
res = []

# 만들어진 순열 조합 전부 확인
for per in A:
    count = 0
    for i in range(n-1):
        # 차이값의 합을 결과에 저장함
        count += (abs(per[i] - per[i+1])) 
    res.append(count)

# 저장한 결과 중 가장 큰 값 출력
print(max(res))