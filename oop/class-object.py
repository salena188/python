class FoodOrder:
    def __init__(self,customer_name, item, price):
        self.customer_name = customer_name
        self.item = item
        self.price = price
    def show_order(self):
        print("Customer Name: {}". format(self.customer_name))
        print("Item: {}". format(self.item))

order1 = FoodOrder("Salina", "pizza", 100)
order2 = FoodOrder("Salina", "pizza", 100)
print(order1.customer_name, order1.item, order1.price)
print(order1.customer_name, order1.price)

'''inside claa : only define methods and attribute
outside class : call methods'''


class Laptop:
    def __init__(self,brand, price):
        self.brand = brand
        self.price = price
    def show_details(self):
        print("Laptop Brand: {}". format(self.brand))
        print("Price: {}". format(self.price))

#create object
laptop1 = Laptop("Acer", 100000)
laptop2 = Laptop("Del", 50000)

#show details
laptop1.show_details()
laptop2.show_details()


