"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle


class Plane(Vehicle):
    cargo = 20
    max_cargo = 20

    def __init__(self, weight, fuel, fuel_consumption, cargo, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo
