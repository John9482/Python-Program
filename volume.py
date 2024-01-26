#Calculate the volume of a sphere
import math
radius = float(input("Please enter the radius of the sphere: "))
volume = 4/3 * math.pi * radius**3
if radius < 0:
        print("Error: Radius must be non-negative.")
else:
        print("The volume of the sphere is",volume)


