class Arnur:
    def __init__    (self, height, weight, size):
        self.height = height
        self.weight = weight
        self.size = size

    def SHOW_MENU(self):
        print(f"His weight is {self.weight}, Height is {self.height}, size is {self.size}")

    def semiru(self):
        self.weight+=50

    def arik(self):
        self.weight = 0 

    def tekseru(self):
        if self.weight > 150:
            print("Tolyk bala")
        else:
            print("Duris Bala")


a1 = Arnur(168, 60, 5)
a2 = Arnur(23645, 7621, 672345)
a3 = Arnur(24526, 4524, 435)
a1.semiru()
a2.tekseru() 
a3.arik()
a3.SHOW_MENU()
        