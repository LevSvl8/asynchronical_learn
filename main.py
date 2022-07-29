

import asyncio
import collections





async def queue_proc(queue): # берем очередь
    # обрабатываем текущий элемент в очереди
    await queue.get()
    # сообщаем о завершении его обработки
    queue.task_done()



async def printa(t,queue):
    await queue.get()
    print(f'{t}')
    queue.task_done()


async def printa_main():
    t_list = [3,4,5]
    tasks = []
    queue = asyncio.Queue()



    for t in t_list:
        tasks.append(printa(t, queue))
        queue.put_nowait(printa(t, queue))

    await queue.join()

    for task in tasks:
        task.cancel()

    await asyncio.gather(*tasks, return_exceptions=True)
    print('done')

    #await asyncio.gather(*tasks)






if __name__ == '__main__':
    asyncio.run(printa_main())



