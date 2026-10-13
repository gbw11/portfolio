expression = input()

# Please write your code here.

letters = list(set(ch for ch in expression if ch.isalpha()))

max_value = float('-inf')

def calculate(mapping):
    result = mapping[expression[0]]
    i = 1

    while i < len(expression):
        op = expression[i]
        num = mapping[expression[i+1]]

        if op == '+':
            result += num

        elif op == '-':
            result -= num

        else: # op : *
            result *= num

        i += 2
    return result


def dfs(idx, mapping):
    global max_value

    if idx == len(letters):
        val = calculate(mapping)
        max_value = max(max_value, val)
        return

    for num in range(1, 5):
        mapping[letters[idx]] = num
        dfs(idx + 1, mapping)
        del mapping[letters[idx]]

dfs(0, {})

print(max_value)