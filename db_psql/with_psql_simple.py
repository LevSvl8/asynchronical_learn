import multiprocessing

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

    def select_one(self, table):
        sql = f'select id from {table}'
        self.cursor = self.conn.cursor()
        self.cursor.execute(sql)
        print(self.cursor.fetchone())

    def insert_into(self,sql):
        self.cursor = self.conn.cursor()
        self.cursor.execute(sql)
        self.conn.commit()
    def select_many(self,table):
        self.cursor = self.conn.cursor()
        for i in range(5000):
            self.cursor.execute(f'select id from {table}')
            print(self.cursor.fetchone())

def select_many(host,dbname,username,password,table):
    conn = psycopg2.connect(
        host=host,
        database=dbname,
        user=username,
        password=password)
    conn.set_client_encoding('UTF8')
    cursor = conn.cursor()
    for i in range(5000):
        cursor.execute(f'select id from {table}')
        print(cursor.fetchone())

def select_row_recorder(host,dbname,username,password,table,file):
    conn = psycopg2.connect(
        host=host,
        database=dbname,
        user=username,
        password=password)
    conn.set_client_encoding('UTF8')
    cursor = conn.cursor()
    cursor.execute(f'select id from {table}')
    res = len(cursor.fetchone())
    print(res)
    with open(file, "w") as f:
        for i in range(1000000):
            f.write(str(cursor.fetchone()))


def main():
    proc1 = multiprocessing.Process(target=select_row_recorder,
                                    args=('localhost', 'learning', 'postgres', 'Afroamerica_2017', 'table_for_py','file'))
    proc1.start()
    proc2 = multiprocessing.Process(target=select_row_recorder,
                                    args=(
                                    'localhost', 'learning', 'postgres', 'Afroamerica_2017', 'one_more', 'file2'))
    proc2.start()
    proc1.join()
    proc2.join()

if __name__ == '__main__':
    starttime = time()
    main()
    print(time() - starttime)
