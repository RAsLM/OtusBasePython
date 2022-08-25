"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
import exceptions


class Plane(Vehicle):
    cargo = 20
    max_cargo = 20

    def __init__(self, weight, fuel, fuel_consumption, cargo, max_cargo):
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
