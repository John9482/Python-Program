class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

    def compute_perimeter(self):
        return 2 * (self.length + self.width)

# Prompt the user to enter the length and width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Create a Rectangle object with the user's input
rectangle = Rectangle(length, width)

# Compute and print the area and perimeter
area = rectangle.compute_area()
perimeter = rectangle.compute_perimeter()
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
