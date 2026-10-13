T = int(input())
for test_case in range(1, T+1):
    n = int(input())    
    station = list(map(int, input().split()))
    stations=station *2
    maximum = 0
 
    for i in range(n):
        for j in range(i+2, i+n-1):
            base = (stations[i]+stations[j])**2
 
            for k in range(i+2, j-1):
                for l in range(k+2, j-1):
                     
                    M = base + (stations[k]+stations[l])**2
                    maximum = max(maximum, M)
                      
             
            for k in range(j + 2, i + n-1):
                for l in range(k + 2, i + n-1):
                     
                    M = base + (stations[k]+stations[l])**2
                    maximum = max(maximum, M)
     
    print(f'#{test_case} {maximum}')