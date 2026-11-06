from abc import ABC, abstractmethod

# =====================================
# Product Class
# =====================================
class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_information(self):
        print(f"Product ID : {self.product_id}")
        print(f"Name       : {self.name}")
        print(f"Price      : ${self.price:.2f}")

    @abstractmethod
    def get_fulfilment_info(self):
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
        super().__init__(product_id, name, price)
        self.weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight     : {self.weight} kg")

    def get_fulfilment_info(self):
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
        super().__init__(product_id, name, price)
        self.download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size : {self.download_size} MB")

    def get_fulfilment_info(self):
        return "Delivered digitally."


# =====================================
# Inventory Class (Aggregation)
# =====================================
class Inventory:

    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product_id: str):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                return True
        return False

    def find_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def display_products(self):
        if not self.products:
            print("Inventory is empty.")
            return

        for product in self.products:
            product.display_information()
            print(product.get_fulfilment_info())
            print("-" * 30)


# =====================================
# Test Aggregation
# =====================================
if __name__ == "__main__":

    print("Prediction:")
    print("The product should still work after being removed")
    print("from an inventory because the inventory only")
    print("stores a reference to the product object.\n")

    # Create Product BEFORE Inventory
    product1 = PhysicalProduct(
        "P001",
        "Gaming Laptop",
        2000.00,
        2.5
    )

    # Create Inventory A
    inventory_a = Inventory()

    print("Adding product to Inventory A...\n")
    inventory_a.add_product(product1)

    inventory_a.display_products()

    print("\nRemoving product from Inventory A...\n")
    inventory_a.remove_product("P001")

    print("Inventory A Contents:")
    inventory_a.display_products()

    print("\nProduct still exists:")
    product1.display_information()

    # Create Inventory B
    inventory_b = Inventory()

    print("\nAdding same product to Inventory B...\n")
    inventory_b.add_product(product1)

    print("Inventory B Contents:")
    inventory_b.display_products()

    print("\nConclusion:")
    print("Removing a product from an inventory")
    print("does not destroy the Product object.")
    print("The product can still be used and")
    print("added to another inventory.")