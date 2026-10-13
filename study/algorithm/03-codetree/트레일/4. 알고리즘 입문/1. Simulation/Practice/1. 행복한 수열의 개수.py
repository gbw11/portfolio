n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

ans = 0
## 가로행 체크
for y in range(n):
    for x in range(n-m+1):
        tmp = []
        for i in range(x, x+m):
            tmp.append(grid[y][i])
        print(tmp[:])
        if len(tmp)==1:
            ans += 1
            break
        else:
            valid = False
            for i in range(len(tmp)-1):
                if tmp[i] != tmp[i+1]:
                    break
                
                valid = True
                ans += 1
            
            if valid:
                break
## 세로 열 체크
for x in range(n):
    for y in range(n-m+1):
        tmp=[]
        for i in range(y, y+m):
            tmp.append(grid[i][x])
        print(tmp)
        if len(tmp)==1:
            ans += 1
            break
        else:
            valid = False
            for i in range(len(tmp)-1):
                if tmp[i] != tmp[i+1]:
                    break
                else:
                    valid = True
                    ans += 1
            if valid:
                break

print(ans)