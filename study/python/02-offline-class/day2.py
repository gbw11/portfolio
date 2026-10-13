# 할당
# list : 가변시퀀스
'''
arr = [1, 2, 3, 4, 5]
print(id(arr))
arr[2]=7
print(id(arr))

arr = [6, 7, 8]
print(id(arr))


arr = [[1,2,3],[4,5,6]]
print(arr[1][0])
print(arr[0][:])
print(arr[1][::-1])

print(len(arr))


# tuple : 불변시퀀스
# 튜플 사용 이유? : 1. 안정성(보안성)
# 알고리즘에서 사용 이유? : 처리속도 빠름(시간복잡도 효율) 
my_tuple = (1,2,3,4,5)

x, y= 1,2 # 튜플이 생략
print(x, y)

def abc(x,y,z):
    return x, y, z # 튜플 생략 return 내부에도
print(abc(1,2,3)) 


# range : 불변 시퀀스
for i in range(13):
    print(i, end = ' ')


#dictionary : 가변비시퀀스

# 1. 하드코딩
my_dict={"apple" : 2,"banana" : 1, "peach" : 3}

# 2. key로 접근
d = dict()
d["apple"] = 2
d["banana"] = 1
d["peach"] = 3

print(my_dict)
print(d)

print(my_dict["banana"])
print(my_dict.keys())  # key만 출력
print(my_dict.values())  # value만 출력
print(my_dict.items())  # 둘다 출력


# set : 가변비시퀀스, 중복 X

my_set = {1, 2, 3, 4}
my_set.add(100)
print(my_set)

# None type

a = None
b = ''
print(type(a))
print(type(b))



# boolean type
print(bool(3)) # 정수는 0을 제외한 모든 수가 True
print(bool(0.0)) # 실수도 0.0을 제외한 모든 수가 True
print(bool("")) # 문자열은 빈문자열을 제외한 모든 문자열이 True
 

# 명시적 형변환
num = 3.5
num = int(float(num))
print(num)

# is
# 1. 데이터 타입까지 판단
# 2. 메모리 주소가 같아야 한다.

print(1 == True) #True
print(1 is True) # False
'''

# 단축평가
print(0 or 1 or 3)
print(2 or 3 or 1)
print(0 and 1)
print(1 and 0 and 3)
print(1 and 2 and 3)

# 가독성 때문에 후행쉼표 붙이기!
arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

print(arr)