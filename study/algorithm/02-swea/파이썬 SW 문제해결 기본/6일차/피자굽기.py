T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split()) #n은 화덕 크기, m은 피자크기
    pizza = list(map(int, input().split()))
    pizza_num = [i for i in range(len(pizza))] # 피자의 번호를 저장하기 위한 리스트 생성
    oven = [] 
    for _ in range(n):  # 초기 오븐 상태 만들기
        oven.append([pizza.pop(0), pizza_num.pop(0)])

    while len(oven) > 1:
        cheese, num = oven.pop(0) # 맨 앞 피자 꺼내기
        cheese //= 2

        if cheese == 0:
            if pizza: #남은 피자 존재하면
                oven.append([pizza.pop(0), pizza_num.pop(0)])
        else:
            oven.append([cheese, num]) # 피자양 반으로 줄여서 젤 뒤로 넣기

    result = oven[0][1] + 1

    print(f'#{tc}', result) 