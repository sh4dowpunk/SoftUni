class Glass:
    initial_content = 0
    capacity = 250

    def __init__(self):
        self.content = self.initial_content

    def fill(self, ml: int) -> str:
        if self.content + ml <= self.capacity:
            self.content += ml
            return f"Glass filled with {ml} ml"

        return f"Cannot add {ml} ml"

    def empty(self) -> str:
        self.content = 0
        return "Glass is now empty"

    def info(self) -> str:
        return f"{abs(self.capacity - self.content)} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
