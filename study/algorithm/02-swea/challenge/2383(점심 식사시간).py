# P : 사람, S : 계단
#
# 계단은 동시에 3명 사용 가능 계단마다 길이가 주어지는데 K분 소요

t = int(input())

for tc in range(1, t+1):
    n = int(input()) # 방의 가로, 세로 길이
    # 1: 사람, 2이상은 계단
    graph = [list(map(int, input().split()))]
