class Personazh:
    def __init__(self, name):
        self.name
    def move(self):
        print(self.name, "Movin")
class Shooterz(Personazh):
    def shoot(self):
        print(self.name, "shot")
class punisherz(Personazh):
    def punch(self):
        print(self.name, "punched")
shelly=Shooterz("shelly")
el_primo=punisherz("el_primo")
pablo=Shooterz("pablo escobar")
shelly.move()
el_primo.punch()
shelly.shoot()
el_primo.move()