from abc import ABC, abstractmethod 
from math import pi

class Shape(ABC):

    def __init__(self,name,color) :
        self.name = name
        self.__color = color 
    
    def getColor(self):
        return self.__color
    
    def setColor(self,color):
        if not isinstance(color,str) :
            print(' color is not string')
        self.__color = color
        print(self.__color)

    @abstractmethod
    def calcArea(self):
        pass


class Circle(Shape):

    def __init___(self,color , radius):
        super(Circle,self).__init__("Circle",color)
        self.__radius = radius

    def getRadius(self):
        return self.__radius
    
    def setRadius(self,radius):
        if(radius <= 0):
            print("can't assign negative number")
            return
        self.__radius = radius

    def calcArea(self):
        return pi * (self.__radius**2)

c1 = Circle("Circle","red")

try:
    c1.setRadius(1)

    print( c1.calcArea() )
    print( c1.getColor() )
except:
    print("Wrong Input")

class Square(Shape):

    def __init__(self,color):
        super(Square,self).__init__("Square",color)
        self.__length 

    def setLength(self,length):
        if(length <= 0):
            print("length Less than equal zero")
            return
        self.__length = length

    def getLength(self):
        return self.__length
    
    def calcArea(self):
        return self.__length**2


try:
    sq1 = Square("Square","blue")
    sq1.setLength(5)

    print( sq1.calcArea())
    print( sq1.getColor())
except:
    print("Wrong length")

class Rectangle(Shape):

    def __init__(self,name,color):
        super(Rectangle,self).__init__(name,color)
        self.__width
        self.__height
        
    def setWidth(self,width):
        if(width <= 0):
            print("length Less than equal zero")
            return
        self.__width = width

    def setHeight(self,height):
        if(height <= 0):
            print("length Less than equal zero")
            return
        self.__height = height
    
    def calcArea(self):
        return self.__width * self.__height 

try:

    rec1 = Rectangle("Square","yellow")
    rec1.setWidth(6)
    rec1.setHeight(5)

    print( rec1.calcArea())
    print( rec1.getColor())
except:
    print("Wrong length")
