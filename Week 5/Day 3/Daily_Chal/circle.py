import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi*(self.radius)**2


circle1 = Circle(4)
print(circle1.area())

    
import turtle

t = turtle.Turtle()

r = 50
t.circle(r)

# r = 10
# n = 10
# for i in range(1, n+1, 1):
#     t.circle(r*i)

# r1 = 20
# r2 = 10
# n = 2
# t.circle(r1) + t.circle(r2)

circles = []

radii = [1, 3, 4, 20, 10, 50]

for radius in radii:
    circles.append(t.circle(radii[radius]))
    print(sort(circles))