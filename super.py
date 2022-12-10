class MobilePhone:
    def touch(self):
        print('providing touching function')

class HTC(MobilePhone):
    def touch(self):
        MobilePhone.touch(self)
        print('Me too.......')



class Weekday():
    def display(self, pay):
        self.price = pay
        print('welcome')
        print('totle price:{}'.format(self.price))

class Holiday(Weekday):
    def display(self, pay):
        super().display(pay)
        if self.price > 1800:
            self.price *= 0.8
        else:
            self.price
        print("20% {}".format(self.price))

monday = Weekday()#父类对象
monday.display(25000)
Christmas = Holiday()#子类对象
Christmas.display(18000)

