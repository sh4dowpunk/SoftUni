from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget

    @property
    @abstractmethod
    def sponsors(self):
        ...

    @property
    @abstractmethod
    def expenses_for_one_race(self):
        ...

        
    @property
    def budget(self):
        return self.__budget
    
    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value  # private attribute, if its public will be recursion a this value = self.budget only
                               # it will try to get new value and will start over again

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0

        for positions in self.sponsors.values():
            for key in positions:
                if race_pos <= key:
                    revenue += positions[key]   # [{1: 1_000_000, 2: 800_000} , {8:.... , 10: }]
                    break   # now break current sponsor and try with next one

        revenue -= self.expenses_for_one_race
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
