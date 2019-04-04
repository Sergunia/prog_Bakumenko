class Goat:
    x = 10 # классовые атрибуты
    y = 20
    m = 30


def walk (goat):
    goat.m += 1


belka = Goat() # классы с большой буквы
strelka = Goat()
belka.x += 100 # атрибут из классового превратился в экземплярный
belka.m = 30
walk (belka)


class Goat:
    x, y = 0, 0
    names []


belka = Goat()
belka.names.append("Белочка") # добавляется элемент Белочка в самом КЛАССЕ

strelka = Goat()




class Goat:
    max_legs_numb = 4
    def __init__(self, x, y): # self  всегда первый):
        # объект-функция (конструктор в классе = метод
        self.x = x
        self.y = y
        self.m = m
        self.names = []
        self._counter = 0
    def show(self): # мы передаем просто сам объект Goat
        print(self.x, self.y, self.m0)
        self._counter += 1 #

belka = Goat(100, 200, 30)
belka.show() # нельзя belka.show(belka) - он воспринимает как подача двух элементов
