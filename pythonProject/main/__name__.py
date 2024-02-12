print("i am before any function")

def area(length,width):
    print("i am in the area function")
    return length*width

if __name__ == "__main__":
    print("this is the main function")
    print(area(2,4))

print("i am outside the main function")
print(area(2,4))