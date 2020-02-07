class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price  *= (1 + percent_change/100)
        else:
            self.price  *= (1 - percent_change/100)

    def print_info(self):
        new_price = "{0:.2f}".format(self.price)
        print(f"Name: {self.name}, price: {new_price}, category: {self.category}")
