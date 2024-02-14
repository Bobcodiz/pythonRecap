import multiprocessing


def calc_square(numbers, result):
    for idx, n in enumerate(numbers):
        result[idx] = n * n
    return


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    result = multiprocessing.Array("i", 5)
    p = multiprocessing.Process(target=calc_square, args=(numbers, result))
    p.start()
    p.join()

    print("the result is :", result[:])
