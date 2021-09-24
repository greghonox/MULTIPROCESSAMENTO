import time
from cython import int, float


def for_f() -> None:
    maxval: int = 0
    total: int = 0
    k: int = 0

    maxval: int = 1_000_000_000
    t1: float = time.time()
    t2: float = time.time()
    t3: float = time.time()

    for k in range(maxval):
        total = total + k

    print("Total =", total)
    t2 = time.time()
    t = t2 - t1
    print("%.10f" % t)
