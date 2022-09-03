"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02 import exceptions


class Plane(Vehicle):
    cargo = 20
    max_cargo = 20

    def __init__(self, weight, fuel, fuel_consumption, max_cargo, cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, weight):
        if (weight + self.cargo) <= self.cargo:
            self.cargo += weight
        else:
            raise exceptions.CargoOverload()

    def remove_all_cargo(self):
        tmp = self.cargo
        self.cargo = 0
        return tmp
