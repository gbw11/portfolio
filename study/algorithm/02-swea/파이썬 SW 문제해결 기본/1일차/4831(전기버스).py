# 전기버스

T = int(input())
for test_case in range(1, T+1):
  K, N, M = map(int, input().split())
  charge_number = list(map(int, input().split()))

# 정류장 번호있는 리스트
  bus_stop_number = [n for n in range(N+1)]
# print(bus_stop_number)

  charge_locate = [0 for n in range(N+1)]

# 충전기 위치에 1 존재하는 리스트
  for i in charge_number:
    charge_locate[i] = 1
# print(charge_locate)

  bus_locate = 0
  charge_count = 0

  while bus_locate +K < N:
    moved = False

    for i in range(K,0,-1):
      if charge_locate[bus_locate+i] == 1:
        bus_locate += i
        charge_count += 1
        moved = True
        break

    if not moved:
      charge_count = 0
      break

  print(f'#{test_case} {charge_count}')