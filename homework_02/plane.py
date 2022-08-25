"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle


class Plane(Vehicle):
    cargo: int = 20
    max_cargo: int = 20

    def __init__(self, weight: int, fuel: int, fuel_consumption: float, cargo: int, max_cargo: int):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo
