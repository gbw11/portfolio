# input()
# Q) input() 실무에서 쓸까??
# A) 실무에서는 input()을 쓰지 않습니다.
# Q) 그런데 왜 input()을 배워야 할까?
# A) 프로그래밍 언어를 단기간에 빠르게 익히는데 가장 좋은방법 : 알고리즘 문제 풀어보는것

# 1. 문자열 하나 입력 받기
char = input()

# 2. 정수 하나 입력받기
char = int(input())

# 3. 정수 2개를 입력받기 (각각의 변수에 할당)
a, b = map(int, input().split())
print(a, b)

# 4. 정수 여러개를 입력받아서 리스트에 할당
arr = list(map(int, input().split()))
print(*arr) # 출력(언패킹연산자 활용)

# 5. 2차원 배열 입력받기 (난이도 D3 문제)
# 반드시 중첩 for문이라는 로직이 필요하다.
# 그런데, 쉬운 방법이 존재 ---> 리스트 컴프리헨션
result = []
for _ in range(3): # 3행
    arr = list(map(int, input().split()))
    result.append(arr)# 1행추가, 2행추가, 3행추가

print(result)

# best 방법 : 리스트컴프리헨션
arr = [list(map(int, input().split())) for _ in range(3)]
print(arr)

# 재귀함수 정의 중요!!!!!!
def kfc(n):
  if n == 2:
    return
  print(n)
  kfc(n+1)
  print(n)

kfc(0)  # 0 1 1 0 출력!!