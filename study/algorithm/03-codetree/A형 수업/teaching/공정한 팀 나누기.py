# n 전체 학생 수 k 팀의 최소 인원수

# 팀워크는 2차원 배열로 준다. 
# 2팀으로 나눌 때 팀워크의 합의 차이 (전력차이)가 최소가 되도록 나누었을 때의 최솟값 
from itertools import combinations

n, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]



people = set()

for i in range(n):
    people.add(i)

ans = 10000
for i in range(1, n//2+1):
    for combo in combinations(people, i):
        team1 = set(combo)
        team2 = people - team1

        cnt1 = 0
        cnt2 = 0

        for i in team1:
            for j in team1:
                cnt1 += graph[i][j]
        
        for i in team2:
            for j in team2:
                cnt2 += graph[i][j]
        
        ans = min(ans, abs(cnt1-cnt2))

print(ans)