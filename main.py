class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []

    def add_item_to_menu(self, item, price):
        self.menu_items[item] = price

    def book_tables(self, table_number):
        self.book_table.append(table_number)

    def customer_order(self, table_number, order):
        order_details = {'table_number': table_number, 'order': order}
        self.customer_orders.append(order_details)

    def print_menu_items(self):
        for item, price in self.menu_items.items():
            print("{}: Rs.{}".format(item, price))

    def print_table_reservations(self):
        for table in self.book_table:
            print("Table {}".format(table))

    def print_customer_orders(self):
        for order in self.customer_orders:
            print("Table {}: {}".format(order['table_number'], order['order']))

# Initialize restaurant
restaurant = Restaurant()

# Add items
restaurant.add_item_to_menu("Biryani", 250)
restaurant.add_item_to_menu("Bihari Kabab", 200)
restaurant.add_item_to_menu("Zinger Burger", 280)
restaurant.add_item_to_menu("Chicken Tikka", 400)
restaurant.add_item_to_menu("Custard", 200)
restaurant.add_item_to_menu("Pulao", 300)
restaurant.add_item_to_menu("Nihari", 200)
restaurant.add_item_to_menu("Haleem", 180)
restaurant.add_item_to_menu("Qorma", 280)
restaurant.add_item_to_menu("Karahi", 400)
restaurant.add_item_to_menu("Drink", 150)
restaurant.add_item_to_menu("Salad", 80)
restaurant.add_item_to_menu("Raita", 80)
restaurant.add_item_to_menu("Roti", 15)
restaurant.add_item_to_menu("Naan", 30)

# Book tables
restaurant.book_tables(1)
restaurant.book_tables(2)
restaurant.book_tables(3)

# Order items
restaurant.customer_order(1, {"Biryani": 1,"Nihari":1, "Roti": 5, "Raita": 1, "Salad": 1,"Drink":2})
restaurant.customer_order(2, {"Pulao": 2,"Karahi":1,"Naan":4,"Salad":1,"Drink":2, "Custard": 2})
restaurant.customer_order(3, {"Pulao": 3,"Qorma":1,"Naan":4,"Salad":1,"Drink":2, "Custard": 2})
print("\nPopular dishes in the restaurant along with their prices:")
restaurant.print_menu_items()

print("\nTables reserved in the Restaurant:")
restaurant.print_table_reservations()

print("\nCustomer orders:")
restaurant.print_customer_orders()
