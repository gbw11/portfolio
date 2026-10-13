n = int(input())
num = list(map(int, input().split()))

# Please write your code here.


path = []
min_cnt = 100
def dfs(lev):
    global min_cnt
    # 마지막 인덱스에 도착하면 함수 호출 종료
    if lev == n-1:
        min_cnt = min(min_cnt, len(path))
        return
    
    # 인덱스 범위 초과를 막기위해서 넘어가는 순간 함수 호출 종료
    elif lev >= n:
        return


    for i in range(1, num[lev]+1):
        path.append(lev)
        dfs(lev + i)
        path.pop()
    

dfs(0)

print(min_cnt if min_cnt != 100 else -1)