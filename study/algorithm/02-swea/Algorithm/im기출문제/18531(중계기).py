T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    Map = []
    for _ in range(N+1):
        Map.append(list(map(int, input().split())))

    x, y = 0, 0

    for i in range(len(Map)):
        for j in range(len(Map)):
            if Map[i][j]==2:
                y, x = i, j
                
        
    c = []
    for i in range(len(Map)):
        for j in range(len(Map)):
            if Map[i][j] == 1:
                hy, hx = i, j
                c.append((hy-y)**2 + (hx-x)**2)

    if max(c)**(1/2)== int(max(c)**(1/2)):
        print(f"#{test_case} {int(max(c)**(1/2))}")
    else:
        r = int(max(c)**(1/2)+1)
        print(f"#{test_case} {r}")