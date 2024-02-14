import math
import time
from multiprocessing import Pool


def jod(n):
    return math.pow(n, 4)


if __name__ == "__main__":
    t1 = time.time()
    pool = Pool()
    for i in range(100):
        results = pool.map(jod,range(1000000))
        print(results)
        total = time.time()-t1
        print(total)
