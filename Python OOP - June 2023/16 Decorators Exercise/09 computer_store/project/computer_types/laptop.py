from project.computer_types.computer import Computer


class Laptop(Computer):
    AVAILABLE_PROCESSOR = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200
    }

    MAX_RAM = 64

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        if processor not in Laptop.AVAILABLE_PROCESSOR:
            raise ValueError(f"{processor} is not compatible with laptop "
                             f"{self.manufacturer} {self.model}!")

        if ram > Laptop.MAX_RAM or not self.power_of_two(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with laptop "
                             f"{self.manufacturer} {self.model}!")

        self.set_parts(processor, ram)
        return f"Created {self.manufacturer} {self.model} with {processor} and " \
               f"{ram}GB RAM for {self.price}$."
