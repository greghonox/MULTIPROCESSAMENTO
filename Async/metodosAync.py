from asyncio import create_task, get_event_loop
from time import time

ARQUIVO = "/home/gregorio/Downloads/jsons.txt"
ARQUIVO_LINKS = "/home/gregorio/Downloads/07-02+-+links.txt"


def ler_normal():
    with open(ARQUIVO, "r") as f:
        arq = f.readlines()
        for linha in arq:
            # print(linha)
            linha


inis = time()
ler_normal()
print(f"TEMPO LEVADO {inis - time()} SERIAL")

from aiofiles import open


async def ler_async1():
    async with open(ARQUIVO) as f:
        arquivo = await f.read()
        # print(arquivo)


async def ler_async2():
    async with open(ARQUIVO) as f:
        async for linha in f:
            # print(linha)
            linha


# ini = time()
# el = get_event_loop()
# el.run_until_complete(ler_async1())
# el.close()
# print(f"TEMPO LEVADO {ini - time()} ASYNC")
# print(f"{'funcao serial e mais rapida' if ini < inis else 'funcao async mais rapida' }")

from aiohttp import ClientSession
from bs4 import BeautifulSoup


async def pegar_links():
    links = []
    async with open(ARQUIVO_LINKS) as f:
        async for linha in f:
            links.append(linha)
    return links


async def pegar_html(link):
    print(f"PEGANDO O LINK {link}")

    async with ClientSession() as s:
        async with s.get(link) as r:
            r.raise_for_status()
            return await r.text()


def pegar_titulo(html):
    s = BeautifulSoup(html, "html.parser")
    return s.find("title").text.split("|")[0]


async def main():
    links = await pegar_links()
    tarefas = []
    for link in links:
        tarefas.append(create_task(pegar_html(link)))

    for tarefa in tarefas:
        html = await tarefa
        titulo = pegar_titulo(html)
        print(f"CURSOS {titulo}")


eel = get_event_loop()
eel.run_until_complete(main())
eel.close()
