import math

shape = input("Enter the shape:")

if shape == "circle":
    radius = int(input("enter the radius: "))
    def circumference(radius):
        Circumference = math.pi * (radius * 2)
        print("the circumference is : ",Circumference)
        return Circumference
    def area(radius):
        Area = math.pi * radius * radius

        print("the area is: ", Area)
        return Area
    circumference(radius)
    area(radius)

elif shape == "rectangle":
    length = int(input("enter the length: "))
    width = int(input("enter the width: "))

    def perimeter(length,width):
        Perimeter =2*length+2*width
        print("the perimeter is:", Perimeter)
        return Perimeter

    def area(length,width):
        Area = length*width
        print("the area is:",Area)
        return Area

    perimeter(length,width)
    area(length,width)



