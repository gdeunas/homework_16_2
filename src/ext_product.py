from src.product import Product


class Smartphone(Product):

    def __init__(
        self, name, description, __price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, __price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if isinstance(other, type(self)):
            self.sum_of_products = float(self.quantity) + float(other.quantity)
            return self.sum_of_products
        raise TypeError


class LawnGrass(Product):

    def __init__(
        self, name, description, __price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, __price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if isinstance(other, type(self)):
            self.sum_of_products = float(self.quantity) + float(other.quantity)
            return self.sum_of_products
        raise TypeError


if __name__ == "__main__":
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    smartphone2 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )

    print(smartphone1 + smartphone2)
