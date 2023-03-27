import time
from contextlib import contextmanager
from collections.abc import Iterator

@contextmanager
def timer() -> Iterator:
    start = time.time()
    try:
        yield
    finally:
        print(time.time() - start)

with timer() as t:
    val = 100 * 100 ** 1000000