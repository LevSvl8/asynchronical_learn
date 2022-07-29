


import asyncio
import psycopg2
from time import time


class MyConn:

    def __init__(self,host,port,dbname, username, password):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.username = username
        self.password = password

    def __enter__(self):
        self.conn = psycopg2.connect(
            host=self.host,
            database=self.dbname,
            user=self.username,
            password=self.password)
        self.conn.set_client_encoding('UTF8')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    async def select_all(self, sql):
        self.cursor = self.conn.cursor()
        await self.cursor.execute(sql)
        self.cursor.fetchone()
        return self.cursor.fetchall()

    def insert_into(self,sql):
        self.cursor = self.conn.cursor()
        self.cursor.execute(sql)
        self.conn.commit()





async def main():
    with MyConn('localhost', 5432,'learning','postgres','Afroamerica_2017') as conn:

        insert = "insert into table_for_py values('Max', 2, 21)"
        #conn.insert_into(insert)

        select = 'select * from table_for_py'
        task1 = asyncio.create_task(conn.select_all(select))
        select = 'select * from one_more'
        task2 = asyncio.create_task(conn.select_all(select))
        print(await task1)
        print(await task2)




if __name__ == '__main__':
    starttime = time()
    asyncio.run(main())
    print(time() - starttime)



