import math

marks = set([80,87,97.100,76,56,89,75,99,77,68])

even_marks = {i for i in marks if i % 2 == 0}
print(even_marks)
root = {math.sqrt(i) for i in marks}
print(root)