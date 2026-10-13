N = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.

# 홀수 => 더해지는 홀수의 갯수가 홀수개

# 짝수 =  더해지는 홀수의 갯수가 0 or 짝수개

odd = [] # 홀
even = [] #짝
for num in numbers: # 홀수 짝수 분리
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

cnt = 0  # cnt: 짝수 면 짝수넣을 차례

if len(odd) > len(even): # 홀수의 갯수가 짝수의 갯수보다 많을때
    del odd[0:len(even)] # odd는 even 갯수만큼 제거

    cnt += len(even)*2
    even.clear() # even 아예 비우고

    # 남은 홀수들로만 나머지 만드는 경우 생각하기(짝수부터 시작)
    quotient = len(odd)//3 # 몫 저장
    if len(odd)%3==1:
        cnt += 2*quotient-1
    elif len(odd)%3==2:
        cnt += 2*quotient+1
    else:
        cnt += 2*quotient

elif len(even) > len(odd):
    del even[0:len(odd)]

    cnt += len(odd)*2
    odd.clear()

    # 남은 짝수들로는 홀수를 만들수 없기 때문에 다 합쳐서 짝수 하나 출력하고 끝
    cnt +=1

else: # 두개의 경우 길이가 같은 경우
    cnt += len(odd)*2  # 번갈아 가면서 한번씩 넣으면 가능

print(cnt)