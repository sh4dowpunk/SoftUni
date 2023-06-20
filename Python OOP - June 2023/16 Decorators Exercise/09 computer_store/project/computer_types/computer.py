from abc import ABC, abstractmethod
from math import log2, floor, ceil


class Computer(ABC):
    AVAILABLE_PROCESSOR = {}

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    @abstractmethod
    def configure_computer(self, processor: str, ram: int):
        pass

    @staticmethod
    def power_of_two(n: int):
        result = log2(n)
        return floor(result) == ceil(result)

    def set_parts(self, processor: str, ram: int):
        self.processor = processor
        self.ram = ram
        self.price += self.AVAILABLE_PROCESSOR[processor]
        self.price += 100 * int(log2(ram))

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
