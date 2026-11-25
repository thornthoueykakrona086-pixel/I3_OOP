class Product:
    store_name = "ITC Online Store"
    product_count = 0

    def __init__(self, name, price, quantity):
        self.name = name 
        self.price = price
        self.quantity = quantity

        Product.product_count += 1

    def display_product(self):
        print("Name:", self.name)
        print("price: $", self.price, sep="")
        print("Quantity:", self.quantity)
        print("Total Value: $", self.total_value(), sep="")

    def total_value(self):
        return self.price * self.quantity

    @classmethod
    def get_product_count(cls):
        return cls.product_count

    @staticmethod
    def is_valid_price(price):
        return price > 0

product1 = Product("Laptop", 1500, 5)
product2 = Product("Mouse", 20, 10)
product3 = Product("Keyboard", 40, 15)

print("========ITC ONLINE STORE ========")

print("\nProduct 1")
product1.display_product()

print("\nProduct 2")
product2.display_product()

print("\nProduct 3")
product3.display_product()

total_inventory = (product1.total_value() + product2.total_value() + product3.total_value())

print("\nTotal Products:", Product.get_product_count())
print("Total Inventory VAlue: $", total_inventory, sep="")