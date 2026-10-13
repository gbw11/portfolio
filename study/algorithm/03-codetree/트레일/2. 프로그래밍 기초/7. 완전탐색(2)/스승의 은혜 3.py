n, b = map(int, input().split())  # n 학생, b 예산
gifts = [tuple(map(int, input().split())) for _ in range(n)]
p = [gift[0] for gift in gifts]  # 선물가격
s = [gift[1] for gift in gifts]  # 배달가격

# Please write your code here.

# 모든 학생에 대해 선물의 가격을 반값 해보고 그때의 최대 학생수를 내보낸다.
# 내보낸 최대 학생수 중에서 의 최댓값을 답으로 도출한다.


result = 0

for i in range(n):
    costs = []

    costs.append(p[i] // 2 + s[i])  # 반값한 친구 추가
    for j in range(n):
        if i != j:
            costs.append(p[j] + s[j])  # 그 외의 친구 추가

    costs.sort()  # 금액 작은순으로 정렬

    cost = 0  # b와 비교하기 위한 학생들의 돈의 합
    cnt = -1  # 학생의 수
    # -1로 두는 이유 : 마지막에 pop에서 금액을 넘으면 그 학생은 추가를 안하는데 밑에서 cnt +1을
    # 한 번더 하기 때문에 애초에 -1에서 시작해서 괴리를 없
    while cost <= b:
        cost += costs.pop(0)  # 앞에서부터 금액 추가
        cnt += 1

    result = max(result, cnt)

print(result)

