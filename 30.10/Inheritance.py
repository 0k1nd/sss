class Building:
    year = None
    city = None
    
    def __init__(self, year, city):
        self.year = year
        self.city = city
        
    def get_info(self):
        print('Year:', self.year, 'City:', self.city)


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
        print('Material:', self.material, 'Area of bUilding:', self.area, 'Color:', self.color, 'Floors:', self.floors)


class School(House):
    people = 0
    def __init__(self, year, city, material, area, color, floors, people):
        super(School, self).__init__(year, city, material, area, color, floors)
        self.people = people
        
    def get_info(self):
        super().get_info()
        print('People:', self.people)


    

class shop(House):
    pass
