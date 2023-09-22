#this is all code that as been done in class
#I have changed the comments to fit my understanding of the solid principles and how this code follows it in my own words
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

# Liskov Substitution Principle, Both the circle and the square can be used as they are both shapes it's not specific to one
# Interface Segregation Principle, The square class only contains what it needs for the squares area nothing else 
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

class AreaCalculator:
    # Single Responsibility Principle (SRP): AreaCalculator calculates the area of different shapes.
    def calculate_area(self, shape):
        return shape.area()


class App:
    # Single Responsibility Principle, this is only responsible for running the code
    def run(self):
        circle = Circle(5)
        square = Square(4)
        
        calculator = AreaCalculator()
        circle_area = calculator.calculate_area(circle)
        square_area = calculator.calculate_area(square)
        
        print("Circle area:", circle_area)
        print("Square area:", square_area)

app = App()
app.run()