

import asyncio

async def to_two():
    for i in range(2):
        print(i)
        await asyncio.sleep(2)

async def to_three():
    for i in range(3):
        print(i)
        await asyncio.sleep(2)

async def to_four():
    for i in range(4):
        print(i)
        await asyncio.sleep(2)

async def to_five():
    for i in range(10):
        print(i)
        if i == 5:
            await to_four()
        await asyncio.sleep(0.2)


async def main():
    tasks = []
#    tasks.append(asyncio.create_task(to_two()))
#   tasks.append(asyncio.create_task(to_three()))
#    tasks.append(asyncio.create_task(to_four()))
    tasks.append(asyncio.create_task(to_five()))
    await asyncio.gather(*tasks)



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

