import random

class Atm:
    def setMoney(self, money):
        self.yellow = money // 50000
        self.green = (money-(self.yellow*50000)) // 10000
        self.red = (money - (self.yellow*50000) - (self.green*10000)) // 5000
        self.blue = (money - (self.yellow*50000) - (self.green*10000) - (self.red*5000)) // 1000
        self.undefined = (money - (self.yellow*50000) - (self.green*10000) - (self.red*5000) - (self.blue*1000))

a = Atm()
moneyyy = random.randint(1000, 100000)
print(moneyyy)
a.setMoney(moneyyy)
print(a.yellow, a.green, a.red, a.blue, a.undefined)