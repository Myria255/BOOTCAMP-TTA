import turtle

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius
    
    def __str__(self):
        return f"Circle(radius={self.radius})"
    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(self.radius + other.radius)
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented


turtle.speed(1)
turtle.color("blue")    
circle1 = Circle(50)
turtle.penup()# Move the turtle to the starting position for the first circle
turtle.goto(-100, 0)
turtle.pendown()
turtle.circle(circle1.radius)
turtle.color("red")

    