from abc import ABC
from exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight: int = 1500
    started: bool = False
    fuel: int = 0
    fuel_consumption: float = 7.8

    def __init__(self, weight: int, fuel: int, fuel_consumption: float):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.started > 0:
                self.started = True
            else:
                raise LowFuelError()

    def move(self, distance):
        if (self.fuel - distance * self.fuel_consumption) > 0:
            self.fuel = self.fuel - distance * self.fuel_consumption
        else:
            raise NotEnoughFuel()
