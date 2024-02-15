import time


def timeit(method):
    def wrapper(func):
        def inner(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"Elapsed time: {end - start}")
            return result
        return inner
    return wrapper(func=method)

