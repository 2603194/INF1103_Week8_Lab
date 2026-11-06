import json
from abc import ABC, abstractmethod


# =====================================
# Interface
# =====================================
class CanBeShipped(ABC):

    @abstractmethod
    def calculate_shipping_cost(self):
        pass


# =====================================
# Abstract Product Class
# =====================================
class Product(ABC):

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def update_stock(self, quantity):
        if self.__stock + quantity >= 0:
            self.__stock += quantity
            return True
        return False

    def display_information(self):
        print(f"Product ID : {self.__product_id}")
        print(f"Name       : {self.__name}")
        print(f"Price      : ${self.__price:.2f}")
        print(f"Stock      : {self.__stock}")

    @abstractmethod
    def get_fulfilment_info(self):
        pass


# =====================================
# Physical Product
# =====================================
class PhysicalProduct(Product):

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = float(weight)

    def get_weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f"Weight     : {self.__weight} kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        return self.__weight * 5


# =====================================
# Digital Product
# =====================================
class DigitalProduct(Product):

    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = float(download_size)

    def get_download_size(self):
        return self.__download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size : {self.__download_size} MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally."


# =====================================
# Inventory Class
# =====================================
class Inventory:

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self):

        if not self.__products:
            print("Inventory is empty.")
            return

        print("\n===== INVENTORY =====")

        for product in self.__products:
            product.display_information()
            print(product.get_fulfilment_info())

            if isinstance(product, PhysicalProduct):
                print(
                    f"Shipping Cost : "
                    f"${product.calculate_shipping_cost():.2f}"
                )

            print("-" * 30)

    def get_products(self):
        return self.__products


# =====================================
# Save Inventory
# =====================================
def save_inventory(inventory):

    data = []

    for product in inventory.get_products():

        if isinstance(product, PhysicalProduct):

            data.append({
                "type": "physical",
                "product_id": product.get_product_id(),
                "name": product.get_name(),
                "price": product.get_price(),
                "stock": product.get_stock(),
                "weight": product.get_weight()
            })

        elif isinstance(product, DigitalProduct):

            data.append({
                "type": "digital",
                "product_id": product.get_product_id(),
                "name": product.get_name(),
                "price": product.get_price(),
                "stock": product.get_stock(),
                "download_size": product.get_download_size()
            })

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory saved successfully.")


# =====================================
# Load Inventory
# =====================================
def load_inventory(inventory):

    try:

        with open("inventory.json", "r") as file:
            data = json.load(file)

        inventory.get_products().clear()

        for item in data:

            if item["type"] == "physical":

                inventory.add_product(
                    PhysicalProduct(
                        item["product_id"],
                        item["name"],
                        item["price"],
                        item["stock"],
                        item["weight"]
                    )
                )

            elif item["type"] == "digital":

                inventory.add_product(
                    DigitalProduct(
                        item["product_id"],
                        item["name"],
                        item["price"],
                        item["stock"],
                        item["download_size"]
                    )
                )

    except FileNotFoundError:
        print("No inventory.json found.")


# =====================================
# Main Program
# =====================================
def main():

    inventory = Inventory()

    load_inventory(inventory)

    while True:

        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            inventory.display_all()

        elif choice == "2":

            print("\n1. Physical Product")
            print("2. Digital Product")

            product_type = input(
                "Select product type: "
            )

            product_id = input("Product ID: ")
            name = input("Product Name: ")
            price = float(input("Price: "))
            stock = int(input("Stock: "))

            if product_type == "1":

                weight = float(
                    input("Weight (kg): ")
                )

                inventory.add_product(
                    PhysicalProduct(
                        product_id,
                        name,
                        price,
                        stock,
                        weight
                    )
                )

            elif product_type == "2":

                download_size = float(
                    input("Download Size (MB): ")
                )

                inventory.add_product(
                    DigitalProduct(
                        product_id,
                        name,
                        price,
                        stock,
                        download_size
                    )
                )

            print("Product added successfully.")

        elif choice == "3":

            product_id = input("Enter Product ID: ")

            product = inventory.search_product(
                product_id
            )

            if product:

                quantity = int(
                    input(
                        "Enter quantity "
                        "to add/remove (+/-): "
                    )
                )

                if product.update_stock(quantity):
                    print("Stock updated successfully.")
                else:
                    print("Stock cannot be negative.")

            else:
                print("Product not found.")

        elif choice == "4":

            product_id = input("Enter Product ID: ")

            product = inventory.search_product(
                product_id
            )

            if product:
                product.display_information()
                print(product.get_fulfilment_info())
            else:
                print("Product not found.")

        elif choice == "5":

            save_inventory(inventory)

        elif choice == "6":

            save_inventory(inventory)
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

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

    if __name__ == "__main__":

        supplier1 = Supplier(
        "S001",
        "Tech Supplies Pte Ltd",
        "sales@techsupplies.com"
    )

    product1 = PhysicalProduct(
        1,
        "Laptop",
        1200.00,
        10,
        2.5
    )

    supplier1.display_information()
    print()
    product1.display_information()
    
main()

