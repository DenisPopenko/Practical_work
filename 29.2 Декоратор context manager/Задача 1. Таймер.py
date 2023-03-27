from contextlib import contextmanager
import time


@contextmanager
def timer():
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(end - start)


def g(h):
    return h ** 3

timer(g(5))