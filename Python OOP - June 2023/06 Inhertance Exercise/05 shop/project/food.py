from project.product import Product


class Food(Product):
    def __init__(self, name):
        super().__init__(name, 15)
        # We are passing the constant 15 to the __init__