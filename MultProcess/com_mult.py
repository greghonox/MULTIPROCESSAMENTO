from multiprocessing import Pipe, Process, Queue


def pingp(conn, msg):
    conn.send(msg)


def pongp(conn):
    msg = conn.recv()
    print(f"MENSAGEM RECEBIDA {msg}")


def pingq(conn, msg):
    conn.put(msg)


def pongq(conn):
    msg = conn.get()
    print(f"MENSAGEM RECEBIDA {msg}")


def main_pipe():
    conn1, conn2 = Pipe(True)

    p1 = Process(target=pingp, args=(conn1, "Jesus esta voltando"))
    p2 = Process(target=pongp, args=(conn2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


def main_queue():
    queue = Queue()

    p1 = Process(
        target=pingq,
        args=(
            queue,
            "Jesus esta voltando",
        ),
    )
    p2 = Process(target=pongq, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


main_pipe()
main_queue()
