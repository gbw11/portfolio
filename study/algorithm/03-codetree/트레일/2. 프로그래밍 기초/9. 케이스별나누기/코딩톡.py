n, m, p = map(int, input().split()) # n: 사람, m ; 메시지 수, p:체크하고싶은 메시지 번호
messages = [tuple(input().split()) for _ in range(m)]
c = [msg[0] for msg in messages]
u = [int(msg[1]) for msg in messages]

# Please write your code here.

p = p - 1 # 리스트에서 찾아야하기때문에 메시지 번호 -1

text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# 참여자 등록
people = [text[i] for i in range(n)]


# 읽은 사람을 등록해서
read_people = []

for i in range(p, m): # p 보다 아래에 친 사람은 무조건 읽었고
    read_people.append(c[i])

for i in range(p, -1, -1): # p 위에 쳤는데 p랑 읽은 사람의 숫자가 같은 사람도 읽었고
    if u[p] == u[i]:
        read_people.append(c[i])
    else: break



# 예외 처리! 다 읽었으면 출력해줄 사람이 없다.
if u[p]==0:
    print('')

else: # 참여자 - 읽은 사람해서 남은 사람을 출력한다.
    result = set(people) - set(read_people)
    print(*result)