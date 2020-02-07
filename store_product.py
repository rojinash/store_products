from product import Product
class Store:
    def __init__(self, name):
        self.name = name
        self.product_list = list()
    
    def add_product(self, new_product):
        self.product_list.append(new_product)

    def sell_product(self, id):
        self.product_list.pop(id)
    
    def inflation(self, percent_increase):
        for product in self.product_list:
            product.update_price(percent_increase, True)
    
    def set_clearance(self, category, percent_discount):
        for product in self.product_list:
            if product.category == category:
                product.update_price(percent_discount, False)
    
    def show_product_info(self):
        for product in self.product_list:
            product.print_info()
            
target = Store('Target')
laptop = Product('Apple Macbook',  1000, 'Electronics')
fan = Product('Cool Fan',  100, 'Electronics')
headphones = Product('Beats',  350.78, 'Electronics')
bananas = Product("Bananas", 4, 'Groceries')


target.add_product(laptop)
target.add_product(fan)
target.add_product(headphones)
target.add_product(bananas)

target.show_product_info()
target.inflation(10)
print("#" * 50)
target.show_product_info()
target.sell_product(1)
print("#" * 50)
target.show_product_info()
target.set_clearance('Electronics', 50)
print("#" * 50)
target.show_product_info()




    