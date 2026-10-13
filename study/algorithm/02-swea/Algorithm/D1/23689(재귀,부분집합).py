arr = ['Luffy', 'Zoro', 'Sanji']

used = ['O', 'X']
path = []

def print_name():
    for i in range(3): # [O, O, X] 같은 형태이기때문에
        if path[i] == 'O':
            print(arr[i], end = ' ')

    print()


def recur(lev):
    if lev == 3:
        print_name()
        return

    for i in range(2):
        path.append(used[i])
        recur(lev+1)
        path.pop()

    return

recur(0)