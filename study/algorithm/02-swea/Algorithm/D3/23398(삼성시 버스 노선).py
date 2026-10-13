T = int(input())
for test_case in range(1, T+1):
    # 5000개의 버스정류장 정의
    bus_stop = [0] * 5001

    n = int(input())
    for i in range(n): #버스 노선 시작, 끝점 받기
        ai, bi = map(int, input().split())
        for j in range(ai, bi+1):
            bus_stop[j] += 1

    p = int(input())
    result = []
    for j in range(p):
        cj = int(input())

        result.append(bus_stop[cj])

    print(f'#{test_case}', *result)