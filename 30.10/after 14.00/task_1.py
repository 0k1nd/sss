class Animal():

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        
    def make_sound(self):
        print(self.sound.upper())
        print('-----')
        
    def description(self):
        print('name:', self.name)
        print('sound:', self.sound)
    
class Dog(Animal):
    
    def __init__(self, name, sound, breed, color):
        super(self).__init__(name, sound)
        self.breed = breed
        self.color = color
        
    def description(self):
        super().description()
        print('breed:', self.breed)
        print('color', self.color)
        print('-----')
        
class Cat(Animal):
    
    def __init__(self, name, sound, breed, color):
        super(self).__init__(name, sound)
        self.breed = breed
        self.color = color
        
    def description(self):
        super().description()
        print('breed:', self.breed)
        print('color', self.color)
        print('-----')
        
        
cat1 = Cat('Lulu', 'бу испугался не бойся я друг я тебя не обижу', 'Sphinx', 'white')
cat1.description()
cat1.make_sound()

dod1 = Dog('qwe', 'gap', 'alabay', 'white')
dod1.description()
dod1.make_sound()
