# coding: utf-8
# license: GPLv3
from gameunit import *

#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.

"""
class Hero(Attacker):

    def __init__ (self, name):
        self._name = name
        self._experience = 0
        self._attack = 50
        self._health = 100

    # def attack (self, target):
     #     target._health -= self.
