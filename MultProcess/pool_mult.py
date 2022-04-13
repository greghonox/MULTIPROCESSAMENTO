from multiprocessing import Pool, Process, cpu_count, current_process


def pegar_nome_processo():
    print(f"NOME DO PROCESSO {current_process().name}")


def calcular(dado, x):
    return dado ** 2


def main():
    tm_pool = cpu_count() * cpu_count()

    print(f"TAMANHO DA POOL {tm_pool}")
    pool = Pool(processes=tm_pool, initializer=pegar_nome_processo)

    entradas = list(range(7)), 1
    saidas = pool.map(calcular, entradas)

    print(f"SAIDAS: {saidas}")

    pool.close()
    pool.join()


main()
