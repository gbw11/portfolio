from collections import deque
t = int(input())
for tc in range(1, t + 1):
    n = int(input())

    adj_matrix = [list(map(int, input().split())) for _ in range(n)]

    people_nums = list(map(int, input().split()))

    # 가장 간단하게 생각하면 1~n//2개까지만 골라서, 고른거에서 가장 최소값을 구하면 되는거 아닌가??


    def is_connected(start, selected):
        que = deque([start])
        visited = [False] * n
        visited[start] = True

        while que:
            start = que.popleft()

            for s in selected:
                if adj_matrix[start][s] == 1 and not visited[s]:
                    que.append(s)
                    visited[s] = True

        if sum(visited) == len(selected):
            return True
        else:
            return False

    def dfs(start, selected, goal):
        global min_cnt

        if len(selected) == goal:
            not_selected = list(set(range(n)) - set(selected))

            if is_connected(selected[0], selected) and is_connected(not_selected[0], not_selected):
                sum_a = sum(people_nums[i] for i in selected)
                sum_b = sum(people_nums[i] for i in not_selected)

                min_cnt = min(min_cnt, abs(sum_a - sum_b))
            return

        for i in range(start, n):
            dfs(i + 1, selected + [i], goal)


    min_cnt = float("inf")

    for i in range(1, n // 2 + 1):
        dfs(0, [], i)

    print(f"#{tc} {min_cnt}")