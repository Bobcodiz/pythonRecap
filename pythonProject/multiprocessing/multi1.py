import math
import multiprocessing as mul
import time


def calc_square(numbers):

    for i in numbers:
        time.sleep(3)
        print("square :", str(i * i))


def calc_cube(numbers):
    for i in numbers:
        time.sleep(3)
        print("cube : ", str(i * i * i))


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]

    p1 = mul.Process(target=calc_square, args=(arr, ))
    p2 = mul.Process(target=calc_cube, args=(arr, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("all done")
