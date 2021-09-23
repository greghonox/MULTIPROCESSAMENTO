from queue import Queue
from random import choice, randint
from threading import Lock, Thread
from time import sleep
from typing import List

lock = Lock()

colors = {
    1: "\033[94m{msg}\033[0;0m",
    2: "\033[93m{msg}\033[0;0m",
    3: "\033[1;35m{msg}\033[0;0m",
    4: "\033[91m{msg}\033[0;0m",
}


class Conta:
    def __init__(self, saldo):
        self.conta = "".join(str(randint(1, 1000)) for _ in range(10))
        self.saldo = saldo

    def __str__(self):
        return f"conta: {self.conta} saldo:{self.saldo}"


def criar_conta() -> List[Conta]:
    return [Conta(saldo=randint(5_000, 10_000)) for i in range(10)]


def transferir(origem: Conta, destino: Conta, valor: int):
    if origem.saldo < valor:
        return

    with lock:
        origem.saldo -= valor
        destino.saldo += valor


def valida_banco(contas: List[Conta], total: int):
    with lock:
        atual = sum(conta.saldo for conta in contas)

    if atual != total:
        print(
            colors[4].format(
                msg=f"ERRO ENCONTRADO NO BALANCO BANCARIO INCOSCIENTE {atual} x {total}"
            )
        )
    else:
        print(colors[1].format(msg=f"TUDO CERTO COM OS VALORES {atual} x {total}"))


def pegar_duas_Contas(contas):
    c1 = choice(contas)
    c2 = choice(contas)

    while c1 == c2:
        c2 = choice(contas)

    print(colors[2].format(msg=f"CONTAS ESCOLHIDAS {c1} {c2}"))
    return c1, c2


def servicos(contas, total):
    for _ in range(1, 10_000):
        c1, c2 = pegar_duas_Contas(contas)
        valor = randint(1, 100)
        transferir(c1, c2, valor)
        valida_banco(contas, total)


def main():
    contas = criar_conta()
    with lock:
        total = sum(conta.saldo for conta in contas)
        print("INICIANDO TRANFERENCIAS")

    tarefas = [
        Thread(
            target=servicos,
            args=(
                contas,
                total,
            ),
        )
        for _ in range(10)
    ]

    [t.start() for t in tarefas]
    [t.join() for t in tarefas]


main()
print("-" * 100)
