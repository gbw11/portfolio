T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    used = [False] * n
    ans = float('inf')

    def recur(lev, current_sum):
        global ans  # 또는 nonlocal (중첩 함수일 경우)
        
        # 가지치기: 현재 합이 이미 최솟값 이상이면 중단
        if current_sum >= ans:
            return
        
        if lev == n:
            ans = min(ans, current_sum)
            return
        
        for col in range(n):
            if used[col]:
                continue
            used[col] = True
            recur(lev + 1, current_sum + arr[lev][col])
            used[col] = False

    recur(0, 0)
    print(f'#{tc}', ans)