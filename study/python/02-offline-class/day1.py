# print함수의 end옵션 default(기본값)는 줄바꿈
# sep옵션 default(기본값)은 공백
# ctrl 누른상태에서 print 함수 마우스 좌클릭
'''
print('hello', end = ' ')
print('world')

print('hello', 'world', sep = '\n')
'''

# 왼쪽이 변수 오른쪽이 value degree변수에 36.5가 저장된다 X
# 변수에 값이 할당된다.
# 값(value)은 메모리 주소를 가르키고, 변수가 메모리를 참조한다.
'''
degree = 36.5
print(id(degree))
print(id(degree))
# 재할당
degree = 36.6
print(id(degree))
'''
# 변수명 규칙 : 숫자로 시작할 수 없다.
# 언더스코어 가능 : _
# 키워드 사용 불가능 : if, for, while
# 내장함수나 메서드는 에러가 나지는 않지만 변수로 사용하지 않는다.
# 대소문자를 구분한다.(서로 다른 유니코드값을 가진다)

'''
arr1 = [1, 2, 3]
# 1arr = [1, 2, 3] X
arr_1 = [1, 2, 3]
# if = 1 X
# for =  1 X
# sum = 10 # 가급적 변수로 사용하지 않는다
print(ord('A'))
print(ord('a'))
'''

# 주석
# 한줄주석 #
# 여러줄 주석 '''
# 단축키로 주석하고싶어 : ctrl + /


# 데이터 타입
'''
a = 2
b = 2.0
c = 3 + 2j # j는 허수
d = '1.3' # 작은따옴표 있으면 무조건 문자열

print(type(a))
print(type(b))
print(type(c))
print(type(d))
'''

# 1억을 지수표현법 (실수형 데이터타입)
'''
num = 1e8
print(type(num))
'''

# 거듭제곱의 우선수위가 제일 높다.
'''
num = -2**2
print(num)
'''

# f-string
'''
name = '홍길동'
age = 24
height = 183.24

print(f'이름은 {name}이고 나이는 {age}이고 키는 {height:.1f}')
'''

# sequence(순서가 존재) type
# 시퀀스 vs 비시퀀스
# 가변(변할수있다) vs 불변(변할수없다)
# 문자열 : 불변시퀀스
# 리스트 : 가변시퀀스

'''
char = 'hello world'
length = len(char)
print(length)
print(char[0], char[-1])
print(char[::2])
print(char[::-1])
'''

