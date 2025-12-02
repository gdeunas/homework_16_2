from src.baseproduct import BaseProduct


class Product(BaseProduct):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        sum_of_products: float = 0,
    ):
        """Для класса Product определите следующие свойства:
        название (name),
        описание (description ),
        цена (price),
        количество в наличии (quantity)."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.sum_of_products = sum_of_products

    def __add__(self, other):
        if isinstance(other, Product):
            self.sum_of_products = float(self.__price) * float(self.quantity) + float(
                other.__price
            ) * float(other.quantity)
            return self.sum_of_products
        raise TypeError

    @classmethod
    def new_product(cls, product):
        return cls(**product)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


if __name__ == "__main__":
    pass
