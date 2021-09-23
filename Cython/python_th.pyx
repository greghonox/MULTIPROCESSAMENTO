import cython
from datetime import datetime
from libc.math cimport sqrt
from multiprocessing import cpu_count
from threading import Thread


def main_th():
    print(f"EXECUTANDO NO COMPUTADOR COM {cpu_count()} NUCLEOS")

    inicio = datetime.now()

    th = []
    for n in range(cpu_count() + 1):
        ini: cython.int = 50_000_000 * (n - 1) / cpu_count()
        fin: cython.int = 50_000_000 * (n - 1) / cpu_count()
        print(f"CORE {n} PROCESSANDO {ini}  ate {fin}")
        th.append(Thread(target=comp, kwargs={"ini": ini, "fin": fin}, daemon=True))

    print(f"HORA INICIAL {inicio}")
    [t.start() for t in th]
    [t.join() for t in th]
    print(f"TEMPO QUE LEVOU {datetime.now() - inicio}")


def main_s():
    print("EXECUTANDO 0 NUCLEOS EM SERIE")

    inicio = datetime.now()

    print(f"HORA INICIAL {inicio}")
    comp(50_000_000)
    print(f"TEMPO QUE LEVOU {datetime.now() - inicio}")


def comp(fin: cython.int, ini: cython.int = 1) -> None:
    pos: cython.int = ini
    fator: cython.int = 1000 * 1000
    while pos < fin:
        pos += 1
        sqrt((pos - fator) * (pos - fator))


main_th()
print("-" * 100)
main_s()
