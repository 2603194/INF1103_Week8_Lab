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
    def __init__(self, product_id: str, name: str,
                 price: float, weight: float):
        super().__init__(product_id, name, price)
        self.weight = weight

    def get_fulfilment_info(self):
        return "Requires physical shipping."


# =====================================
# Digital Product
# =====================================
class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str,
                 price: float, download_size: float):
        super().__init__(product_id, name, price)
        self.download_size = download_size

    def get_fulfilment_info(self):
        return "Delivered digitally."


# =====================================
# OrderLine Class
# =====================================
class OrderLine:

    def __init__(self, product: Product, quantity: int):
        self.product: Product = product
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity

    def display_information(self):
        print(
            f"{self.product.name} x {self.quantity} "
            f"= ${self.calculate_subtotal():.2f}"
        )


# =====================================
# Order Class
# =====================================
class Order:

    def __init__(self, order_id: str):
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

    def remove_order_line(
        self,
        product_id: str
    ) -> bool:

        for line in self.order_lines:
            if line.product.product_id == product_id:
                self.order_lines.remove(line)
                return True

        return False

    def calculate_total(self) -> float:
        total = 0

        for line in self.order_lines:
            total += line.calculate_subtotal()

        return total

    def display_order(self):
        print(f"\n===== ORDER {self.order_id} =====")

        for line in self.order_lines:
            line.display_information()

        print(
            f"Order Total = "
            f"${self.calculate_total():.2f}"
        )


# =====================================
# Test Composition
# =====================================
if __name__ == "__main__":

    print("Prediction:")
    print(
        "If the same Product is added to "
        "two Orders, there will be"
    )
    print("2 OrderLine objects but only")
    print("1 Product object.\n")

    # Products
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

    # Order 1
    order1 = Order("O001")

    order1.add_order_line(
        laptop,
        2
    )

    order1.add_order_line(
        course,
        3
    )

    order1.display_order()

    # Order 2
    order2 = Order("O002")

    order2.add_order_line(
        laptop,
        1
    )

    order2.display_order()

    print("\n===== OBJECT COMPARISON =====")

    print(
        "Same Product Object?"
    )

    print(
        order1.order_lines[0].product
        is
        order2.order_lines[0].product
    )

    print(
        "\nOrderLine Objects Same?"
    )

    print(
        order1.order_lines[0]
        is
        order2.order_lines[0]
    )

    print("\nRemoving Laptop from Order 1")

    order1.remove_order_line(
        "P001"
    )

    order1.display_order()

    print(
        "\nOrder 2 still has its own "
        "OrderLine:"
    )

    order2.display_order()

    print(
        "\nProduct still exists:"
    )

    laptop.display_information()