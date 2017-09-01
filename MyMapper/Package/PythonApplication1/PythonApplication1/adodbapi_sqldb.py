import adodbapi
	
def try_connection():


    config = dict(provider='SQLOLEDB',
                  server=   'RAJASENTHIL\SQLEXPRESS',
                  port=      1433,                   
                  database= 'Taxi',
                  username= 'sa',
                  password= 'shambhavvi')

    conn_string = 'Provider=%s;Data Source=%s;Initial Catalog=%s;User ID=%s;Password=%s;' % ( config['provider'],config['server'],
                                                                                             config['database'], config['username'], config['password'] )
    conn= adodbapi.connect(conn_string)

    return conn


cn=try_connection()

cursor=cn.cursor()

cursor.execute('select * from dbo.sales')

for entry in cursor:
    print(entry)

