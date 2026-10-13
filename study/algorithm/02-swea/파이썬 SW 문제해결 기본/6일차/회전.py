T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    
    i = m % n
    
    print(f'#{tc}', numbers[i])
