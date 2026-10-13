# import sys
# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

t = int(input())

for tc in range(1, t+1):
    # n 직원의 수 b 선반의 높이
    n, b = map(int, input().split())
    # 직원들의 키 배열
    arr = list(map(int, input().split()))

    path = []
    ans = b
    def recur(start):
        global ans
        if sum(path)>=b:
            ans = min(sum(path)-b, ans)
            return

        # 조합
        for i in range(start, n):
            path.append(arr[i])
            recur(i+1)
            path.pop()
    recur(0)
    print(f'#{tc}', ans)