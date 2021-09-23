from asyncio import get_event_loop, sleep


async def hello():
    print("OIII")
    await sleep(1)
    print("PRONTO")


el = get_event_loop()
el.run_until_complete(hello())
el.close()
