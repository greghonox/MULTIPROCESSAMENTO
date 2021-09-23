from asyncio import Queue, gather, get_event_loop, sleep
from datetime import datetime


async def gerar_dados(qtde: int, dados: Queue):
    print(f"QUANTIDADE {qtde} DADOS")
    for idx in range(qtde + 1):
        item = idx * idx
        await dados.put((item, datetime.now()))
        await sleep(0.001)

    print(f"QUANTIDADE DADOS {qtde} DADOS GERADO COM SUCESSO")


async def processando_dados(qtde: int, dados: Queue):
    print(f"AGUARDANDO O PROCESSAMENTO DE {qtde} DADOS...")
    processados = 0
    while processados < qtde:
        await dados.get()
        processados += 1
        await sleep(0.0001)
    print(f"FORAM PROCESSADOS {processados} ITENS")


async def run(total, dados):
    await gerar_dados(total, dados)


total = 5_000
dados = Queue()
el = get_event_loop()
el.run_until_complete(run(total, dados))
el.run_until_complete(gerar_dados(total, dados))
el.run_until_complete(gerar_dados(total, dados))
el.run_until_complete(processando_dados(total * 3, dados))
el.close()

print("PARALELO")

total = 5_000
dados = Queue()

el = get_event_loop()
t1 = el.create_task(gerar_dados(total, dados))
t2 = el.create_task(gerar_dados(total, dados))
t3 = el.create_task(gerar_dados(total, dados))
t4 = el.create_task(processando_dados(total * 2, dados))

print("INICILIZANDO PARALELO")
tarefas = gather(t1, t2, t3)
el.run_until_complete(tarefas)
el.close()
