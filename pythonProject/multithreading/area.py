import math
import threading
import time


def circle_area(radius):
    area = math.pi * math.pow(radius, 2)
    return area


def triangle_area(base, height):
    area = (base * height) / 2
    return area


def square_area(side):
    return side * side


radius = float(input("Enter the radius of the circle: "))
side = float(input("Enter the side of the square: "))
base = float(input("Enter the base of the trangle: "))
height = float(input("Enter the height of the triangle: "))
start_time = time.time()
print(circle_area(radius), triangle_area(base, height), square_area(side))
end_time = time.time()
print("this took", end_time - start_time, "seconds")

A1 = threading.Thread(target=circle_area, args=(radius,))
A2 = threading.Thread(target=triangle_area, args=(base, height))
A3 = threading.Thread(target=square_area, args=(side,))

start = time.time()
A1.start()
A3.start()
A2.start()

stop = time.time()
total = stop - start
time.sleep(1)
A1.join()
A2.join()
A3.join()

print("completed th jobs after :",total*1000)