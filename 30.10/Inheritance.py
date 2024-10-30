class Building:
    year = None
    city = None
    
    def __init__(self, year, city):
        self.year = year
        self.city = city
        
    def get_info(self):
        print('Year:', self.year,'|', 'City:', self.city)


class House(Building):
    material = None
    area = 0
    color = None
    floors = 0
    
    def __init__(self, year, city, material, area, color, floors):
        super(House, self).__init__(year, city)
        self.material = material
        self.area = area
        self.color = color
        self.floors = floors
        
    def get_info(self):
        super().get_info()
        print('Material:', self.material,'|', 'Area of bUilding:', self.area,'m**2','|', 'Color:', self.color,'|', 'Floors:', self.floors)


class School(House):
    people = 0
    def __init__(self, year, city, material, area, color, floors, people):
        super(School, self).__init__(year, city, material, area, color, floors)
        self.people = people
        
    def get_info(self):
        super().get_info()
        print('People:', self.people)    

class Shop(House):
    def __init__(self, year, city, material, area, color, floors, stores_profit = 0, fullness_of_the_products = 0):
        super(Shop, self).__init__(year, city, material, area, color, floors)
        self.stores_profit = stores_profit
        self.fullness_of_the_products = fullness_of_the_products
        
    def get_info(self):
        super().get_info()
        print('stores profit =', self.stores_profit, '$ per mounth')
        print('fullness_of_the_products =', self.fullness_of_the_products, '%')

class Drug_store(Shop):
    pass
     
pharmacy = Drug_store(1944, 'New York', 'concrete', 1256, 'red', 2, 1200, 98)

pharmacy.get_info()