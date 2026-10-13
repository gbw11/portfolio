# n명을 3개의 분반으로 나눈다.


# 분반의 기준이 되는 점수 t1, t2

# t2 <= A반
# t1 <= B반 < t2
# C반 < t1

# 최대 반의 인원수와 최소 반은 인원수의 차를 최소로 하는
# t1, t2 설정하기
# 한반 1명이상

# 분반 불가능 할 경우 -1

t = int(input())

for tc in range(1, t+1):
    # n 신입사원수, s : 반 최소 인원, l : 반 최대인원
    n, s, l = map(int, input().split())

    scores = list(map(int, input().split()))
    min_score = min(scores)
    max_score = max(scores)
    best_diff = float("inf")
    for t1 in range(min_score, max_score):
        for t2 in range(t1+1, max_score+1):
            num1 = 0
            num2 = 0
            num3 = 0
            for score in scores:
                if score < t1 :
                    num1 += 1
                elif t1<= score<t2:
                    num2 += 1
                else:
                    num3 += 1
            # 각 반이 1명 이상인지 확인
            if num1 < 1 or num2 < 1 or num3 < 1:
                continue

            # s, l 제약 조건 확인 (문제에 따라 필요시 사용)
            if not (s <= num1 <= l and s <= num2 <= l and s <= num3 <= l):
                continue

            # print(num1, num2, num3)
            diff =max(num1, num2, num3)-min(num1, num2, num3)
            best_diff = min(diff, best_diff)

    if best_diff == float("inf"):
        print(f"#{tc}", -1)
    else:
        print(f'#{tc}', best_diff)