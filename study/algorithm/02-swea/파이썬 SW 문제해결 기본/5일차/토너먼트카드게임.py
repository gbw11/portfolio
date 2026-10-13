T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    card = list(map(int, input().split()))

    players = [(i+1,card[i]) for i in range(len(card))]
    # 번호와 카드 튜플로 패킹

    def rps(a,b):

        if a[1]==b[1] or (a[1]==1 and b[1]==3) or (a[1]==2 and b[1]==1) or (a[1]==3 and b[1]==2):
            return a
        return b

    def tournament(players):
        if len(players) == 1:
            return players[0]

        mid = (len(players)+1)//2 # 홀수일 경우 왼편이 한명더 많아야 하기 때문에
        left = tournament(players[:mid])
        right = tournament(players[mid:])

        return rps(left, right)

    winner = tournament(players)
    print(f'#{test_case}', winner[0])