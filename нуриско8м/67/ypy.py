class Hero:
    def __init__(self,name,health,armor,power,weapon):
        self.name=name 
        self.helth=health
        self.armor=armor
        self.power=power
        self.wepon=weapon
    def hello(self):
        print('привет!я',self.name)
        print("здоровье",self.health)
        print("броня",self.armor)
    def attack(self,enemy):
        print(self.name,"наносит удар по",enemy.name)
        enemy.armor-=self.power
        if enemy.armor<0:
            enemy.health+=enemy.armor
            enemy.armor=0
knight=Hero("karl",100,100,40,"нож")
soldiers=Hero("dream",100,25,60,"арматура")
