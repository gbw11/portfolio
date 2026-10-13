## 격자 안에서의 완전탐색

'''
'격자' ==='이차원배열' ==='범위가 벗어났는지 여부'

예시그림
(x,y) (x+1,y)(x+2,y)

for x in range(n):
    for y in range(n):
        #(x, y)
        #(x+1, y)
        #(x+2, y)
        => coin

        result = max(result, coin)

print(result)
'''
#====== 강사님 코드 구현=======
dys = [0,0,0,1,1,1,2,2,2]
dxs = [0,1,2,0,1,2,0,1,2]

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

for y in range(n - 2):
    for x in range(n - 2):
        # 주어진 영역 내에서 coin의 개수를 센다.
        
        coin = 0
        for dy, dx in zip(dys, dxs):
            coin += [y + dy][x + dx]

        result = max(result, coin)

print(result)

#=== 재귀함수에 대한 설명  + 위 코드 재귀로 만들어보기
'''
1. 파라미터에 무엇을 넣을지
2. 함수가 어떤 값을 리턴할지
3. 종료조건
'''
'''
def recur(y, x, i):
    if i >8:
        return 0
    
    ty = y + dys[i]
    tx = x + dxs[i]

    return recur(y, x, i-1) + grid[y][x]
'''