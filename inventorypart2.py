from abc import ABC, abstractmethod

# =====================================
# Product
# =====================================
class Product(ABC):

    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int
    ):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(
        self,
        quantity: int
    ) -> None:
        self.stock += quantity

    def display_information(self) -> None:
        print(f"ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Stock: {self.stock}")

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass


# =====================================
# Physical Product
# =====================================
class PhysicalProduct(Product):

    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        weight: float
    ):
        super().__init__(
            product_id,
            name,
            price,
            stock
        )

        self.weight = weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.weight}kg")

    def get_fulfilment_info(self) -> str:
        return "Requires physical shipping."


# =====================================
# Digital Product
# =====================================
class DigitalProduct(Product):

    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        download_size: float
    ):
        super().__init__(
            product_id,
            name,
            price,
            stock
        )

        self.download_size = download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size: {self.download_size}MB")

    def get_fulfilment_info(self) -> str:
        return "Delivered digitally."


# =====================================
# Inventory
# =====================================
class Inventory:

    def __init__(self):
        self.products: list[Product] = []

    def add_product(
        self,
        product: Product
    ) -> None:
        self.products.append(product)

    def display_all_products(
        self
    ) -> None:

        print("\n===== INVENTORY =====")

        for product in self.products:
            product.display_information()
            print(product.get_fulfilment_info())
            print("-" * 30)


# =====================================
# LSP Test Function
# =====================================
def show_product_details(
    product: Product
) -> None:

    product.display_information()
    print(product.get_fulfilment_info())
    print("-" * 30)


# =====================================
# Test Program
# =====================================
if __name__ == "__main__":

    physical = PhysicalProduct(
        "P001",
        "Gaming Laptop",
        2000.00,
        10,
        2.5
    )

    digital = DigitalProduct(
        "D001",
        "Python Course",
        99.99,
        100,
        500
    )

    print("===== LSP TEST =====")

    show_product_details(physical)
    show_product_details(digital)

    inventory = Inventory()

    inventory.add_product(physical)
    inventory.add_product(digital)

    inventory.display_all_products()
