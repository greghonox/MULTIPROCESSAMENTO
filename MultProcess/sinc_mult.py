from multiprocessing import Lock, Process, Value


def sacar_s_lock(saldo):
    for _ in range(10_000):
        saldo.value -= 1


def depositar_s_lock(saldo):
    for _ in range(10_000):
        saldo.value += 1


def sacar_lock(saldo, lock):
    with lock:
        for _ in range(10_000):
            saldo.value -= 1


def depositar_lock(saldo, lock):
    with lock:
        for _ in range(10_000):
            saldo.value += 1


def transacao_lock(saldo):
    lock = Lock()
    p1 = Process(
        target=depositar_lock,
        args=(
            saldo,
            lock,
        ),
    )
    p2 = Process(
        target=sacar_lock,
        args=(
            saldo,
            lock,
        ),
    )

    p1.start()
    p2.start()

    p1.join()
    p2.join()


def transacao_s_lock(saldo):
    p1 = Process(
        target=depositar_s_lock,
        args=(saldo,),
    )
    p2 = Process(
        target=sacar_s_lock,
        args=(saldo,),
    )

    p1.start()
    p2.start()

    p1.join()
    p2.join()


saldo = Value("i", 100)
transacao_lock(saldo)
print(f"valor com lock {saldo.value}")

saldo = Value("i", 100)
transacao_s_lock(saldo)
print(f"valor com SEM lock {saldo.value}")
