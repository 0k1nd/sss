class cat:
    name = None
    age = None
    color = None
    isHappy = None
    
    def __init__(self, name = None, age = None, color = None, isHappy = None):
        self.set_data(name, age, color, isHappy)
    
    def set_data(self, name = None, age = None, color = None, isHappy = None):
        self.name = name
        self.age = age
        self.color = color
        self.isHappy = isHappy
        
    def get_data(self):
        print(self.name)
        print(self.age)
        print(self.color)
        print(self.isHappy)
        
cat1 = cat('ede', 3, 'red', True) 
cat2 = cat()

cat1.get_data()
print('----------------')
cat2.get_data()