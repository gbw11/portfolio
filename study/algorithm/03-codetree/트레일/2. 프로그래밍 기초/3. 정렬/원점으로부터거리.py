n = int(input())
points = [(int(i), tuple(map(int, input().split()))) for i in range(n)]

# Please write your code here.
result = []
for point in points:
    x, y = point[1][0], point[1][1]
    idx = point[0]
    distance = abs(x) + abs(y) # 거리 계산
    if not result: # 비어있으면
        result.append((idx, distance)) #(인덱스, 거리)를 넣기
    else:
        for i in range(len(result)):
            if distance < result[i][1]: # 거리 비교해서 작아지는 위치 발견하면
                result.insert(i, (idx,distance)) # 그 바로 앞에 집어넣기
                break
        else:
            result.append((idx, distance)) # 작아지는게 없으면 제일 큰거기 때문에 젤 뒤에 삽입

for re in result:
    print(re[0] + 1) # 인덱스를 1부터 줬기 때문에 +1

