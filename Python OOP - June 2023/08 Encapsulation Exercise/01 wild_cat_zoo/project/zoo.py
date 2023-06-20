from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        if price > self.__budget:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_money_needed_for_salaries = 0
        # sum(worker.salary for worker in self.workers)
        for worker in self.workers:
            total_money_needed_for_salaries += worker.salary
        if total_money_needed_for_salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_money_needed_for_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_money_needed_for_animals = 0
        # sum(animal.money_for_care for animal in self.animals)
        for animal in self.animals:
            total_money_needed_for_animals += animal.money_for_care
        if total_money_needed_for_animals > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_money_needed_for_animals
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = [animal for animal in self.animals if isinstance(animal, Lion)]
        tigers = [animal for animal in self.animals if isinstance(animal, Tiger)]
        cheetahs = [animal for animal in self.animals if isinstance(animal, Cheetah)]
        result += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            result += f"{lion.__repr__()}\n"
        result += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            result += f"{tiger.__repr__()}\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            result += f"{cheetah.__repr__()}\n"
        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keepers = [keeper for keeper in self.workers if isinstance(keeper, Keeper)]
        caretakers = [caretaker for caretaker in self.workers if isinstance(caretaker, Caretaker)]
        vets = [vet for vet in self.workers if isinstance(vet, Vet)]
        result += f"----- {len(keepers)} Keepers:\n"
        for lion in keepers:
            result += f"{lion.__repr__()}\n"
        result += f"----- {len(caretakers)} Caretakers:\n"
        for tiger in caretakers:
            result += f"{tiger.__repr__()}\n"
        result += f"----- {len(vets)} Vets:\n"
        for cheetah in vets:
            result += f"{cheetah.__repr__()}\n"
        return result.strip()