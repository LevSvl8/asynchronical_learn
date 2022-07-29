
import asyncio






async def copy_table(table,uid):
    global boole
    boole = True
    print(f'select {uid} from {table}')
    boole = False
    await compare_and_copy()
    print('hi')


async def compare_and_copy():
    temp_dict = {'MAXVARS':['MAXVARS','ID']}
    res = []

    task2 = asyncio.create_task(wa)

    for tbl_dict in temp_dict.values():
        table, uid = tbl_dict[0], tbl_dict[1]
        asyncio.create_task(copy_table(table, uid))
        res.append(await copy_table(table, uid))

    return res


if __name__ == '__main__':

    asyncio.run(compare_and_copy())