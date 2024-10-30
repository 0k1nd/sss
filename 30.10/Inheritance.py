class Building:
    year = None
    city = None
    def __init__(self, year = None, city =None):
        self.year = year
        self.city = city
        
    def get_info(self):
        print('Year:', self.year, 'City:', self.city)

class School(Building):
    pass        


school = School(2000, 'moscow')
minimarket = Building(2000, 'moscow')
house = Building(2000, 'moscow')

