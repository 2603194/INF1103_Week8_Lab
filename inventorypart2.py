from abc import ABC, abstractmethod

# =====================================
# Product
# =====================================
class Product(ABC):

    def __init__(
        self,
        product_id: str,
        name: str,
        price: float
    ):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_information(self) -> None:
        print(f"Product ID : {self.product_id}")
        print(f"Name       : {self.name}")
        print(f"Price      : ${self.price:.2f}")

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
        weight: float
    ):
        super().__init__(
            product_id,
            name,
            price
        )

        self.weight = weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight     : {self.weight} kg")

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
        download_size: float
    ):
        super().__init__(
            product_id,
            name,
            price
        )

        self.download_size = download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"Download Size : {self.download_size} MB")

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

            print(
                product.get_fulfilment_info()
            )

            print("-" * 30)


# =====================================
# Function Using Product Abstraction
# =====================================
def show_product_details(
    product: Product
) -> None:

    product.display_information()

    print(
        product.get_fulfilment_info()
    )

    print("-" * 30)


# =====================================
# Test Program
# =====================================
if __name__ == "__main__":

    print("Prediction:")
    print("PhysicalProduct -> Requires physical shipping.")
    print("DigitalProduct -> Delivered digitally.\n")

    laptop = PhysicalProduct(
        "P001",
        "Gaming Laptop",
        2000.00,
        2.5
    )

    course = DigitalProduct(
        "D001",
        "Python Course",
        99.99,
        500
    )

    inventory = Inventory()

    inventory.add_product(
        laptop
    )

    inventory.add_product(
        course
    )

    print("\n===== POLYMORPHISM TEST =====")

    for product in inventory.products:

        product.display_information()

        print(
            product.get_fulfilment_info()
        )

        print("-" * 30)

    print("\n===== show_product_details() =====")

    show_product_details(laptop)

    show_product_details(course)