from queue import Queue
from random import randint
from threading import Thread
from time import sleep

colors = {
    1: "\033[94m{msg}\033[0;0m",
    2: "\033[93m{msg}\033[0;0m",
    3: "\033[1;35m{msg}\033[0;0m",
    4: "\033[91m{msg}\033[0;0m",
}


def gerador_dados(queue):
    for i in range(11):
        print(colors[randint(1, 4)].format(msg=i))
        sleep(2)
        queue.put(i)


def consumidor_dados(queue):
    while queue.qsize() > 0:
        valor = queue.get()
        print(colors[randint(1, 4)].format(msg=valor))
        queue.task_done()
        sleep(1)


queue = Queue()
th1 = Thread(target=gerador_dados, args=(queue,))
th2 = Thread(target=consumidor_dados, args=(queue,))

th1.start()
th1.join()
print("-" * 200)
th2.start()
th2.join()
