import pyodbc


config = dict(DRIVER='{ODBC Driver 11 for SQL Server}',
                server=   'RAJASENTHIL\SQLEXPRESS',
              port=      1433,                   
              database= 'Taxi',
              username= 'sa',
              password= 'shambhavvi')



#conn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER='+config['server']+';DATABASE='+config['database']+';UID='+config['username']+';PWD='+ config['password'])

conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER='+config['server']+';DATABASE='+config['database']+';UID='+config['username']+';PWD='+ config['password'])

#conn=pyodbc.connect(**config)
cursor=conn.cursor()

cursor.execute('select * from dbo.sales')

for entry in cursor:
    print(entry)

