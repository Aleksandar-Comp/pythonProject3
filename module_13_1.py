import asyncio

async def start_strongman(name, power):
    print(f"Силач {name} начал соривнование")

    for i in range(1, 6):
        print(f"Силач {i} поднял {name}")
        await asyncio.sleep(1 / power)

    print(f"Силач {name} закончил соривнования")

async def start_tournament():
    participants = [("Pasha", 3), ("Denis", 4), ("Apollon", 5)]

    tasks = [start_strongman(name, power) for name, power in participants]
    await asyncio.gather(*tasks)

asyncio.run(start_tournament())

