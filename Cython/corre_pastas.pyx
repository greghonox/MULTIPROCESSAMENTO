from os import walk
from os.path import join
from cython import char

RAIZ: char = "/proc"


def correr_pastas():
    return [join(x, i) for x, y, z in walk(RAIZ) for i in z]
