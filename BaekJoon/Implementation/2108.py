# 문제
# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다.
# 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다.
# 단, N은 홀수라고 가정하자.
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다.
# 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

# 출력
# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 둘째 줄에는 중앙값을 출력한다.
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 넷째 줄에는 범위를 출력한다.

from collections import Counter
import sys

num = int(input())
num_list = []
mean = 0
mid = 0
rang = 0

for i in range(num):
    num_list.append(int(sys.stdin.readline()))

# 산술 평균
mean = round(sum(num_list) / num)
# 정렬 후
num_list = sorted(num_list)
# 중앙값
mid = num_list[round(num // 2)]
# 최빈값
# Counter는 ' 값 : 갯수 ' 형태의 dict 을 반환, most common 을 이용해서 많은 순으로 정렬 
most = Counter(num_list)
most = most.most_common()
# 범위 
rang = max(num_list) - min(num_list)

print(mean)
print(mid)
# word 가 한개 이상일 때 만 동일 최빈값 중 2번째로 작은 값을 구하는 코드 실행
if len(most) > 1:
    if most[0][1] == most[1][1]:
        print(most[1][0])
    else:
        print(most[0][0])
else:
    print(most[0][0])
print(rang)

