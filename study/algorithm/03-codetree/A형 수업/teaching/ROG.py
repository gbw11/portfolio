이차원 격자 => r(0), o(1), g(2)

0,1  로는 이동 x
2 로만 이동 o

1 영역 => a주기로 1 > 2 > 0 > 1 ...

'''
코디가 이동하기 전에 변동사항을 반영

코디는 이동할 수도 있고, 머무를 수도 있다.

g칸에 올라가고 머물러 있다가 r, o 로 바뀌는건 ok
'''
'''
a = 3

t = 0
c 2 1 0
2 0 2 2
2 0 0 2
2 2 2 2

t =1
2 c 1 0
2 0 2 2
2 0 0 2
2 2 2 2

t=2
2 c 1 0
2 0 2 2
2 0 0 2
2 2 2 2

t=3  ==> a=3 이여서 1이 2로 이동함
2 2 c 0
2 0 2 2
2 0 0 2
2 2 2 2

t=4
2 2 1 0
2 0 c 2
2 0 0 2
2 2 2 2

t=5
2 2 1 0
2 0 2 c
2 0 0 2
2 2 2 2
'''

이차원 격자에서 A => B로 이동하는 거리 ::: BFS(dist, visited)

BFS인데 뭐가 다르지?

0 ~ a-1초 : 1
a ~ 2a-1초 : 2
2a ~ 3a-1초 : 0

def bfs():
    while q:
        x, y, cnt = q.popleft()
        current_time = dist[x][y] + cnt # 현재시간

        for i in range(4):
            nx = x + dxs[i]
            ny = y + dys[i]

            if visited[nx][ny] = True:
                continue
    
            # town[nx][ny]가 0 or 1 or 2 일수 있다.


            if town[nx][ny]==1:
                # town[nx][ny]의 다음 값
                expected = (((current_time + 1) // a) + 1) % 3
                if expected in [0, 1]:
                    continue
            
            # 초기에 1이 현재 어떤 값을 가질까?(현재시간 확인 필요)
            
            if town[nx][ny] == 0:
                continue


            if (0, 1): # 방문할 곳의 좌표가 아닌 경우
                continue

            visited[nx][ny] = True
            dist[nx][ny] = min(dist[nx][ny], dist[y][x] + cnt +1)
            q.append(nx, ny, 0)

        if cnt >= 3 *a:
                continue
            
        visited[x][y] = True
        q.append((x, y, cnt+1))
    



#======== 강사님이 주신 코드 =======

def bfs():
    while q:
        x, y, cnt = q.popleft()
        current_time = dist[x][y] + cnt

        for i in range(4):
            nx = x + dxs[i]
            ny = y + dys[i]

            if visited[nx][ny]:
                continue

            if town[nx][nx] == 0:
                continue

            if town[nx][ny] == 1:
                # town[nx][ny]의 다음 값
                expected = (((current_time + 1) // a) + 1) % 3
                if expected in [0, 1]:
                    continue

            visited[nx][ny] = True
            dist[nx][ny] = min(dist[nx][ny], dist[y][x] + cnt + 1)
            q.append((nx, ny, 0))

        if cnt >= 3 * a:
            continue

        visited[x][y] = True
        q.append((x, y, cnt + 1))
