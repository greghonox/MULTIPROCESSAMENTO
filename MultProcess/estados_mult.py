from ctypes import c_bool
from multiprocessing import Process, Value
from time import sleep


def fun1(val, stat):
    if stat:
        res = val + 10
    else:
        res = val + 20
        val = 200
    stat = not stat
    print(f"O RESULTADO DA FUNC1 {res}")
    return val, stat


def fun2(val, stat):
    if stat:
        res = val + 30
    else:
        res = val + 40
        val = 400
    stat = not stat
    print(f"O RESULTADO DA FUNC2 {res}")
    return val, stat


def fun3(val, stat):
    if stat.value:
        res = val.value + 10
    else:
        res = val.value + 20
        val.value = 200
    stat.value = not stat.value
    print(f"O RESULTADO DA FUNC1 {res}")
    return val, stat


def fun4(val, stat):
    if stat.value:
        res = val.value + 30
    else:
        res = val.value + 40
        val.value = 400
    stat.value = not stat.value
    print(f"O RESULTADO DA FUNC2 {res}")
    return val, stat


def main():
    valor = 100
    status = False

    p1 = Process(
        target=fun1,
        args=(
            valor,
            status,
        ),
    )
    p2 = Process(
        target=fun2,
        args=(
            valor,
            status,
        ),
    )

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("PROCESSOS COMPARTILHADOS")
    valor = Value("i", 100)
    status = Value(c_bool, False)
    p1 = Process(
        target=fun3,
        args=(
            valor,
            status,
        ),
    )
    p2 = Process(
        target=fun4,
        args=(
            valor,
            status,
        ),
    )

    p1.start()
    p2.start()

    p1.join()
    p2.join()


main()
