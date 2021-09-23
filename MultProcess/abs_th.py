from concurrent.futures.thread import ThreadPoolExecutor as Executer
from multiprocessing import Process
from threading import Thread
from time import sleep


def processar():
    print("[", end="", flush=True)
    for _ in range(11):
        print("#", end="", flush=True)
        sleep(1)
    print("]", end="", flush=True)
    return 7


th = Thread(target=processar)
th.start()
th.join()

th = Process(target=processar)
th.start()
th.join()

with Executer() as e:
    exec = e.submit(processar)
    print(f"\nO retorno e {exec.result()}")
