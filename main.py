class Hero():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def is_alive(self):
        return self.health > 0

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атаковал {other.name}")
        print(f"У {other.name} осталось {other.health} здоровья")


class Game():
    def __init__(self):
        self.player = Hero('Player')
        self.computer = Hero('Computer')

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"Игра окончена. {self.player.name} победил!")
                break

            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"Игра окончена. {self.computer.name} победил!")
                break


Game().start()