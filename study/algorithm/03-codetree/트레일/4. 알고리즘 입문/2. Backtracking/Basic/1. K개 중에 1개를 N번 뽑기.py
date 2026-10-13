K, N = map(int, input().split())

# Please write your code here.

answer = []


def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print("")


def get_num(curr_num):
    if curr_num == N + 1:
        print_answer()
        return

    for select in range(1, K + 1):
        answer.append(select)
        get_num(curr_num + 1)
        answer.pop()

    return


get_num(1)