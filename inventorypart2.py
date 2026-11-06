from abc import ABC, abstractmethod

# =====================================
# Supplier Class
# =====================================
class Supplier:
    def __init__(self, supplier_id, name, contact_email):
        self.__supplier_id = supplier_id
        self.__name = name
        self.__contact_email = contact_email

    def get_supplier_id(self):
        return self.__supplier_id

    def get_name(self):
        return self.__name

    def get_contact_email(self):
        return self.__contact_email

    def display_information(self):
        print(f"Supplier ID   : {self.__supplier_id}")
        print(f"Name          : {self.__name}")
        print(f"Contact Email : {self.__contact_email}")


# =====================================
# Product Class
# =====================================
class Product(ABC):
    def __init__(self, product_id, name, price, stock_quantity, supplier: Supplier):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
        self.supplier: Supplier = supplier

    def display_information(self):
        print(f"Product ID : {self.product_id}")
        print(f"Name       : {self.name}")
        print(f"Price      : ${self.price:.2f}")
        print(f"Stock      : {self.stock_quantity}")

    def display_supplier_information(self):
        self.supplier.display_information()

    @abstractmethod
    def get_fulfilment_info(self):
        pass


# =====================================
# Physical Product
# =====================================
class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock_quantity,
                 supplier, weight):
        super().__init__(
            product_id,
            name,
            price,
            stock_quantity,
            supplier
        )
        self.weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight     : {self.weight} kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."


# =====================================
# Digital Product
# =====================================
class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock_quantity,
                 supplier, download_size):
        super().__init__(
            product_id,
            name,
            price,
            stock_quantity,
            supplier
        )
        self.download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size : {self.download_size} MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally."


# =====================================
# Test Association
# =====================================
if __name__ == "__main__":

    supplier1 = Supplier(
        "S001",
        "Tech Supplies Pte Ltd",
        "sales@techsupplies.com"
    )

    physical_product = PhysicalProduct(
        "P001",
        "Gaming Laptop",
        2000.00,
        10,
        supplier1,
        2.5
    )

    digital_product = DigitalProduct(
        "D001",
        "Python Course",
        99.99,
        100,
        supplier1,
        5.0
    )

    print("===== SUPPLIER =====")
    supplier1.display_information()

    print("\n===== PHYSICAL PRODUCT =====")
    physical_product.display_information()

    print("\nSupplier Information Through Product:")
    physical_product.display_supplier_information()

    print("\n===== DIGITAL PRODUCT =====")
    digital_product.display_information()

    print("\nSupplier Information Through Product:")
    digital_product.display_supplier_information()

    print("\nDeleting supplier variable...")
    del supplier1

    print("\nSupplier still accessible through products:")

    print("\nPhysical Product:")
    physical_product.display_supplier_information()

    print("\nDigital Product:")
    digital_product.display_supplier_information()