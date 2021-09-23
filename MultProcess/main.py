from multiprocessing import Process, current_process

print(f"INICIANDO O PROCESSO COM O NOME {current_process().name}")


def faz_algo(valor):
    print(f"FAZENDO ALGO COM O VALOR {valor}")


def main():
    pc = Process(target=faz_algo, args=("Passarinho",), name="Euu")
    pc.start()
    pc.join()


main()
