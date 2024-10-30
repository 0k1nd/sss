class Car:
    brand = None
    model = None
    year = 0
    mileage = 0
    engine_started = False
    __fuel_level = 10
    
    def __init__(self, brand, model, year, mileage, engine_started = False):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.engine_started = engine_started
   
    def get_fuel_level(self):
        print('you`re fuel level = ', self.__fuel_level)
        print('----')
        
    
    def start_enegine(self):
        if self.engine_started is False:
            self.engine_started = True
            print('starting engine...')
        else:
            self.engine_started = False 
            print('engine turning off...')
        print('----')          
    
    def get_info(self):
        print('name:', self.brand, self.model)
        print('year:', self.year)
        print('mileage:', self.mileage)
        if self.engine_started == False:
            print('engine not work')
        else:
            print('engine working')
        print('---------------')
                 
    def refuel(self, liters):
        if self.__fuel_level + liters > 100:
            self.__fuel_level = 100
            print('you overfilled the gasoline')
        else:
            self.__fuel_level = self.__fuel_level + liters
            print('now you`re Fuel level = ', self.__fuel_level)
        print('---')   
        
    def drive(self, miles):
        self.mileage = self.mileage + miles
        print('you`ve drive', miles)
        print('now mileage =', self.mileage)
        print('---')
        
mycar = Car('toyota', 'corolla', 2000, 32000)
mycar.get_info()
mycar.start_enegine()
mycar.get_info()
mycar.start_enegine()
mycar.drive(123)
mycar.get_info()
mycar.get_fuel_level()
mycar.refuel(23)
mycar.get_fuel_level()
mycar.refuel(231234)
mycar.get_fuel_level()
mycar.get_info()

