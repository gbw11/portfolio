class SetMenu:
    # 생성자 메서드
    def __init__(self):
        self.potato = 100
        self.hambug = 400

    #메서드
    def eat_menu(self):
        print("햄버거 세트 굿")
        print(f"{self.potato + self.hambug} 비용이 들었다.")

# 클래스 호출(변수 + 클래스명())
# 인스턴스 생성
betodi = SetMenu()

# 메서드 호출
betodi.eat_menu()

#=================================
a = 3
b =[1, 3, 2, 5, 4]
c = SetMenu()
a = 15
b[3] = 2 # 할당 x
a = SetMenu()

# Q1 변수의 개수는 몇개? 3개
# Q2 객체의 개수는 몇개? 11개 1+6+1+1+1+1  : 2번째 줄에서 리스트 만다는 할당(1) + 각 원소할당(5) = 6
# Q3 할당 횟수는 몇번? 5번
