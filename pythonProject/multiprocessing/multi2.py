import math
import time
import multiprocessing


def area(side):
    n = 0
    while n < 5:
        time.sleep(5)
        print("the area is :", side * side)
        n += 1
    return


def volume(side):
    n = 1
    while n < 5:
        time.sleep(5)
        print("the volume is:", math.pow(side, 3))
        n += 1


if __name__ == '__main__':
    side = int(input("enter the side"))

    p1 = multiprocessing.Process(target=area, args=(side,))
    p2 = multiprocessing.Process(target=volume, args=(side,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("done")
