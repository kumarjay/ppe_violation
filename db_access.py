import pyodbc
import pandas as pd

def connection():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=RAMADHELPD3ITD;'
                          'Database=PPE_VIOLATION;'
                          'Trusted_Connection=yes;')

    return conn

# cursor = conn.cursor()
# cursor.execute('SELECT * FROM PPE_VIOLATION.dbo.ppe_vio')
#
#
#
# sql_query = pd.read_sql_query(f'SELECT * FROM PPE_VIOLATION.dbo.ppe_vio', conn)


