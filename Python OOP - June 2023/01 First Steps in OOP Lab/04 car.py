class Car:
    def __init__(self, name, model, engine):
        self.name: str = name
        self.model: str = model
        self.engine: str = engine

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"


car = Car("Kia", "Rio", "1.3L B3 I4")
print(car.get_info())