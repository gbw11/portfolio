T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    k = 1  # 처음만 동쪽
    findnumber = 1
    cnt = 0
    before_x, before_y = 0, 0
 
    while True:
        found = False
        for i in range(N):
            for j in range(N):
                if arr[i][j] == findnumber:
                    dx = i - before_x
                    dy = j - before_y
 
                    dirs = []
                    if dx < 0: dirs.append(0)  # 북
                    if dy > 0: dirs.append(1)  # 동
                    if dx > 0: dirs.append(2)  # 남
                    if dy < 0: dirs.append(3)  # 서
 
                    
                    d1, d2 = dirs
                    c1 = (d1 - k) % 4 + (d2 - d1) % 4
                    c2 = (d2 - k) % 4 + (d1 - d2) % 4
 
                    if c1 <= c2:
                        cnt += c1
                        k = d2
                    else:
                        cnt += c2
                        k = d1
 
                    before_x, before_y = i, j
                    findnumber += 1
                    found = True
                    break
            if found:
                break
        if not found:
            break
 
    print(f"#{test_case} {cnt}")