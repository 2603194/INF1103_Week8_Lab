from abc import ABC, abstractmethod

# =====================================
# Supplier
# =====================================
class Supplier:

    def __init__(
        self,
        supplier_id: str,
        name: str,
        contact_email: str
    ):
        self.supplier_id: str = supplier_id
        self.name: str = name
        self.contact_email: str = contact_email

    def display_information(self) -> None:
        print(f"Supplier ID: {self.supplier_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.contact_email}")


# =====================================
# Product
# =====================================
class Product(ABC):

    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        supplier: Supplier
    ):
        self.product_id: str = product_id
        self.name: str = name
        self.price: float = price
        self.supplier: Supplier = supplier

    def display_information(self) -> None:
        print(f"ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")

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
        supplier: Supplier,
        weight: float
    ):
        super().__init__(
            product_id,
            name,
            price,
            supplier
        )

        self.weight: float = weight

    def get_fulfilment_info(self) -> str:
        return "Physical shipping required"


# =====================================
# Digital Product
# =====================================
class DigitalProduct(Product):

    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        supplier: Supplier,
        download_size: float
    ):
        super().__init__(
            product_id,
            name,
            price,
            supplier
        )

        self.download_size: float = download_size

    def get_fulfilment_info(self) -> str:
        return "Digital download"


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

    def remove_product(
        self,
        product_id: str
    ) -> bool:

        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                return True

        return False

    def find_product(
        self,
        product_id: str
    ) -> Product | None:

        for product in self.products:
            if product.product_id == product_id:
                return product

        return None


# =====================================
# OrderLine
# =====================================
class OrderLine:

    def __init__(
        self,
        product: Product,
        quantity: int
    ):
        self.product: Product = product
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity


# =====================================
# Order
# =====================================
class Order:

    def __init__(
        self,
        order_id: str
    ):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(
        self,
        product: Product,
        quantity: int
    ) -> None:

        order_line = OrderLine(
            product,
            quantity
        )

        self.order_lines.append(order_line)

    def calculate_total(self) -> float:

        total: float = 0.0

        for line in self.order_lines:
            total += line.calculate_subtotal()

        return total


# =====================================
# Testing
# =====================================
if __name__ == "__main__":

    supplier = Supplier(
        "S001",
        "Tech Supplies",
        "sales@techsupplies.com"
    )

    laptop = PhysicalProduct(
        "P001",
        "Laptop",
        1200.00,
        supplier,
        2.5
    )

    course = DigitalProduct(
        "D001",
        "Python Course",
        99.99,
        supplier,
        500
    )

    inventory = Inventory()

    inventory.add_product(laptop)
    inventory.add_product(course)

    order = Order("O001")

    order.add_order_line(laptop, 2)
    order.add_order_line(course, 1)

    print(f"Order Total: ${order.calculate_total():.2f}")
