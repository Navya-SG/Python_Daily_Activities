#
import math
radius = int(input())
diameter=2*radius
circumference=round(2*math.pi*radius)
area=round(math.pi*radius**2)
print(f"For a radius of:{radius}")
print("Diameter:",diameter)
print("Circumference:",circumference)
print("Area:",area)

#
import math
def diameter(radius):
    return 2 * radius
def circumference(radius):
    return round(2 * math.pi * radius)
def area(radius):
    return round(math.pi * radius ** 2)

'''
from circle_utils import diameter,circumference,area
radius=int(input())
print(f"For a radius of:{radius}")
print("Diameter:",diameter(radius))
print("Circumference:",circumference(radius))
print("Area:",area(radius))''' #error

