import multiprocessing
import time


def calc_square(numbers, queue):
    for n in numbers:
        time.sleep(2)
        queue.put(n * n)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6]
    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=calc_square, args=(numbers, queue))

    p.start()
    p.join()

    while queue.empty() is False:
        print(queue.get())
