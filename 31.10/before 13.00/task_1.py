class Item:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __str__(self):
        return f"{self.name}, {self.price}"
    
class Order:
    
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
        
    def remove_item(self, item):
        self.items.remove(item)
        
    def calculate_total(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        print('total price =', total_price)
        
    def display_order(self):
        print('Your order')
        for i, element in enumerate(self.items):
            print((i + 1), element)
        self.calculate_total()          
            
class Customer:
    
    def __init__(self, name):
        self.name = name
        self.order = Order()
        
    def create_order(self):
        pass
    
    def add_to_order(self, item):
        self.order.add_item(item)
        
    def finalize(self):
        self.order.display_order()
    
it1 = Item('pasta', 120)
it2 = Item('meat', 999)
it3 = Item('cofe', 1670)
it4 = Item('tea', 140)
it5 = Item('egg', 1)
it6 = Item('bread', 13)

men1 = Customer('Bil')
men1.create_order()
men1.add_to_order(it1)
men1.add_to_order(it2)
men1.add_to_order(it6)
men1.add_to_order(it3)
men1.finalize()
        
    
        
        
    