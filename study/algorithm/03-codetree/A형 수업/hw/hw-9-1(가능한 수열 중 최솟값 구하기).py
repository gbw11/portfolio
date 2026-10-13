n = int(input())

# Please write your code here.


path = []

# 겹치는 부분있는지 확인 하는 함수
def is_good():
    length = len(path)
    for size in range(1, length//2 + 1):
        # 뒤에서부터 하나씩 늘려가면서 체크하기
        if path[-size:] == path[-2*size: -size]:
            return False

    return True

def recur(lev):
    if lev == n:
        print(''.join(map(str, path)))
        exit()

    
    for num in range(4, 7):
        path.append(num)

        if is_good():
            recur(lev + 1)

        path.pop()

recur(0)