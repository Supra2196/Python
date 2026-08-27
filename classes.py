#Cost Calculator 
class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def get_total_value(self):
        return self.price*self.quantity
    def update_quantity(self,new_qty):
        self.quantity = new_qty
item=Product("Laptop",1000,5)
#Original Cost of Laptop
print(item.get_total_value())
#Inflated Cost of Laptop
item.update_quantity(3)
print(item.get_total_value())
#Company Supplier Information
class Supplier:
    def __init__(self, company_name, contact_email):
        self.company_name=company_name
        self.contact_email = contact_email
    def display_info(self):
        print(f"{self.company_name}  {self.contact_email}")
    def update_contact(self,new_email):
        self.contact_email=new_email
supplier= Supplier("John Doe Shipping","JDShipping@gmail.com")
supplier.display_info()
#Company Inventory
class Inventory:
    def __init__(self):
        self.products = []
    def add_product(self,product):
        self.products.append(product)
    def get_total_inventory(self):
        total=0
        for product in self.products:
            total += product.get_total_value()
        return total
    def list_all_products(self):
        for product in self.products:
            print(f"{product.name} ${product.price} x {product.quantity} =${product.get_total_value()}")
product1 = Product("Laptop",1000,5)
product2 = Product("Mouse",25,20)
product3 = Product("Keyboard",75,10)
inventory=Inventory()
inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_product(product3)
inventory.list_all_products()
print(f"Total Inventory Value: ${inventory.get_total_inventory()}")
