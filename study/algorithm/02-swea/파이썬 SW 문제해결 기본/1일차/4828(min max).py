T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    test = list(map(int,input().split()))

    M = max(test)
    m = min(test)
    print(f"#{test_case} {M-m}")
