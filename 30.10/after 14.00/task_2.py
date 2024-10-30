import abc
class Shape (abc.ABC):
    
    @abc.abstractmethod
    def area(self):
        pass
    
    def description(self):  
        print (self.__class__.__name__)
        
class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        area = self.radius * self.radius * 3.14
        print('area =', area)
        print('---')
    
    def __str__(self):
        print('Circle')
        print('radius =', self.radius)
        print('area =', self.radius ** 2 * 3.14)
        print('---')
        
class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        area = self.side ** 2
        print('area =', area)
        print('---')
        
    def __str__(self):
        print('Square')
        print('side =', self.side)
        print('area =', self.side ** 2)
        print('---')
    
abcd = Square(4)
michail = Circle(3)
abcd.area()
abcd.description()
abcd.__str__()
michail.area()
michail.description()
michail.__str__()