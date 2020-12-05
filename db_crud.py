import datetime
from datetime import date, time
import pandas as pd
import db_access


conn= db_access.connection()


def read(conn):
    print('Read...')
    cursor = conn.cursor()
    #     cursor.execute('select * from Table_2 where SrNo= ?', (3))

    #     for row in cursor:
    #         print(f'row : {row}')
    sql_query = pd.read_sql_query(f'SELECT * FROM PPE_VIOLATION.dbo.ppe_vio where SrNo=2', conn)
    return sql_query


# cursor = conn.cursor()
# cursor.execute(
#     "insert into ppe_vio(Date, Time, Helmet, Jacket, Shoes, Camera, Image) values(?,?,?,?,?,?,?)",
#     (date.today().strftime('%Y-%m-%d'), datetime.time(datetime.now()).strftime('%H:%M:%S'),
#      dict_[2], dict_[1], dict_[4], f'LM_{cam}', f'{cam}_000{ii}.jpg'))
conn.commit()

def create(d1, d2, d3, cam, ii):
    print('Create')
    cursor = conn.cursor()
    cursor.execute("insert into ppe_vio(Date, Time, Helmet, Jacket, Shoes, Camera, Image) values(?,?,?,?,?,?,?)",
                   (date.today().strftime('%Y-%m-%d'), datetime.time(datetime.now()).strftime('%H:%M:%S'),
                    d1, d2, d3, f'LM_{cam}', f'{cam}_000{ii}.jpg'))
    conn.commit()
    read(conn)
    return 'Done....'


def update(conn):
    print('Update')
    cursor = conn.cursor()
    cursor.execute('update Table_2 set co;= ? where col= ?;', ())
    conn.commit()
    read(conn)


def delete(conn):
    print('Delete')
    cursor = conn.cursor()
    cursor.execute('delete from Table_2 where a>5')
    conn.commit()
    read(conn)
