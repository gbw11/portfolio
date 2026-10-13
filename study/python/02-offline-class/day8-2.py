# 상속을 하는 이유(상속하면 할 수 있는 것)
# 1. 부모 메서드를 교체(오버라이딩)
# 2. 새로운 메서드를 추가

#부모 클래스
class Person:
    def walk(self):
        print("사람이 걷는다.")

    def introduce(self):
        print("나는 공병우")


# 자식 클래스
# 상속: 자식 클래스의 인자로 부모클래스가 들어간다.
class Captain(Person):
    def fly(self): # 메서드
        print("캡틴 코리아 난다")

    def walk(self): # 오버라이딩(메서드 재정의)
        print("캡틴이 걷는다.")

    def introduce(self):
        super().introduce() # 부모 클래스의 메서드를 호출하기 위해
        print("그리고 나는 캡틴 코리아")

a = Captain() # 인스턴스 생성

a.walk()
a.fly()
a.introduce()

# 다중 상속
# 클래스의 정의 순서가 아닌 상속 순서가 중요
# MRO(Method resolution Order)

