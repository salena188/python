class FoodOrder:   #creating a class named FoodOrder
    def __init__(self,customer_name, item, price): #initializing the attributes of class
        self.customer_name = customer_name #assigining the value of customer_name to instance variable
        self.item = item
        self.price = price

    def show_order(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Item: {self.item}")
        print(f"Price: {self.price}")
        # print("Customer Name: {}". format(self.customer_name))
        # print("Item: {}". format(self.item))

order1 = FoodOrder("Salina", "pizza", 100) #passing the value
order2 = FoodOrder("Ben", "burger", 50)
print(order1.customer_name, order1.item, order1.price)  #accessing customer_name attribute of order1
print(order2.customer_name, order2.item, order2.price)  #acessing item attribute of order2
#order1.show_order()


'''inside claa : only define methods and attribute
outside class : call methods'''


class Laptop:
    def __init__(self,brand, price):
        self.brand = brand
        self.price = price

    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Price: {self.price}")

#create object
laptop1 = Laptop("Acer", 100000)
laptop2 = Laptop("Del", 50000)

#show details
laptop1.show_details()
laptop2.show_details()


