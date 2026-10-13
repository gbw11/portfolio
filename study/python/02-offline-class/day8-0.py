class Jugling:

    def __init__(self, hp =20, mana =50):
        self.hp = hp
        self.mana = mana
    

    def run(self):
        print("run!")
        self.hp -=1
        self.mana +=1

    def show_status(self):
        print(f"hp: {self.hp}", f"mana: {self.mana}", sep = "\n")

z1 = Jugling()
z2 = Jugling()

z1.run()
z1.show_status()

for _ in range(5):
    z2.run()

z2.show_status()