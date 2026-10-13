T = int(input())

arr = [i for i in range(1, 13)]
for test_case in range(1, T + 1):
  n, k = map(int, input().split())

  cnt = 0


  def dfs(arr, n, k, idx=0, current=[]):
    global cnt
    #   목표값 초과하면 바로 탈출(가지치기)
    if len(current) > n or sum(current) > k:
      return

    if idx == len(arr):
      if len(current) == n and sum(current) == k:
        cnt += 1
      return
    # 현재원소 포함 x
    dfs(arr, n, k, idx + 1, current)
    # 현재 원소 포함 o
    dfs(arr, n, k, idx + 1, current + [arr[idx]])


  dfs(arr, n, k)
  print(f'#{test_case}', cnt)



## 강민이가 보내준 코드
'''

for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())

    cnt = 0

    def dfs(pick_num, num_sum, n, k, start):
        # print(pick_num) # 어떤 식으로 돌아가는지 확인용
        global cnt

        if num_sum > k: # 초과하면 스탑
            return

        if len(pick_num) == n and num_sum == k: # 카운팅 되는 조건이면 카운트
            cnt += 1
            return

        elif len(pick_num) < n: # 아직 n개 못골랐을 때
            for i in range(start, 13): # 전체 순회하면서

                if num_sum + i > k: # 만약 이때까지 뽑은 숫자의 합 + 이번에 뽑을 것 > k 이면 스탑
                    break

                answer = pick_num + [i] # 뽑은 숫자 넣고 재귀
                dfs(answer, num_sum + i, n, k, i + 1)

    dfs([], 0, n, k, 1)
    print(f"#{t} {cnt}")


'''