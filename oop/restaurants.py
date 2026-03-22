class Restaurant:
    # class variable
    menu ={
        "Pizza": 500,
        "Burger": 300,
        "Mo:mo": 200,
        "Salad": 150,
        "Soda": 100,
        "Ice cream": 80
    }
    def __init__(self, customer_name):
        # object attribute
        self.customer_name = customer_name # value passed during object creation
        self.order = [] # list to store ordered items
        self.order_summary = {} # dictionary to store item and quantity
        self.discount = 0 # value to store discount percentage

    # order process for customer
    def place_order(self,item,quantity):
        # objects attribute
        if item in Restaurant.menu:
            price = Restaurant.menu[item]* quantity
            order = (item, quantity, price) # tuple to store item, quantity and price
            self.order.append(order) # add order to the order list
            # update dictionary with item and quantity
            self.order_summary[item] = self.order_summary.get(item, 0) + quantity
        else:
            print(f"{item} is not available in the menu.")
            # print("Order placed successfully")

    # method to calculate total price and apply discount
    def apply_discount(self, discount_percentage):
        self.discount = discount_percentage
        print(f"Applying {self.discount}% discount to customer{self.customer_name}.")

    # calculate total price after applying discount
    def calculate_total(self):
        total_func = lambda order: order[2] # calculate total price using lambda function
        total = sum(total_func(order) for order in self.order) # calculate total price using sum function
        if self.discount>0:
            total = total - (total * self.discount / 100) # apply discount to total price
        return total

    # unique items ordered using set data structure
    def unique_items(self):
        return set(item[0] for item in self.order) # return unique items ordered using set comprehension

    def show_summary(self):
        print("\n------ Order Summary for", self.customer_name, "------")
        print("Item-wise quantity (dictionary):", self.order_summary)
        print("Unique items ordered (set):", self.unique_items())
        print("Discount applied:", self.discount, "%")
        print("Total bill after discount:", self.calculate_total())
        print("--------------------------------------\n")


customer1 = Restaurant("Veronica")
customer2 = Restaurant("Ben")

#place orders
customer1.place_order("Pizza", 1)
customer1.place_order("Mo:mo", 2)
customer1.place_order("Soda", 1)
customer1.place_order("Ice cream", 2)
customer1.apply_discount(10) # apply 10% discount for customer1

customer2.place_order("Salad", 2)
customer2.place_order("Soda", 1)
customer2.apply_discount(5) # apply 5% discount for customer2

# show order summary for both customers
customer1.show_summary()
customer2.show_summary()