class Human():
    def __init__(self, name:str, age:int, health:int):
        self._name = name
        self._age = age
        self._health = health

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, valve:str):
        self._name = valve

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, valve:int):
        self._age = valve

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, valve:int):
        self._health = valve

class Thing():
    def __init__(self, name:str, sale:int, prochnost:int):
        self._name = name
        self._sale = sale
        self._prochnost = prochnost

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, valve:str):
        self._name = valve

    @property
    def sale(self):
        return self._sale

    @sale.setter
    def sale(self, valve:int):
        self._sale = valve

    @property
    def prochnost(self):
        return self._prochnost

    @prochnost.setter
    def prochnost(self, valve:int):
        self._prochnost = valve