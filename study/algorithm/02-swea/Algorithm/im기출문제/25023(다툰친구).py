
# A~Z까지 모두 다른 알파벳으로 구성된 네글자 입력받기

text = input()

#네글자 중에서  B,T가 붙어있지 않은 경우의 수 출력하기

result = []
cnt = 0

def recur(idx = 0):
    global cnt
    if idx == 4:
        for i in range(len(result)-1): # B, T 붙어 있는 경우 체크하기 위함
            if ((result[i] == 'B' and result[i+1] == 'T')
                   or (result[i] =='T' and result[i+1] == 'B')):
                break
        else: cnt += 1
        return

    for ch in text: # result 에 문자 넣는경우
        result.append(ch)
        recur(idx+1)
        result.pop()
    return

recur()
print(cnt)
