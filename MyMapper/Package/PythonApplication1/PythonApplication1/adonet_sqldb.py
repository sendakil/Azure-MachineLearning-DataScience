

import clr, os
clr.AddReference("System.Data")
import System.Data.OleDb as ADONET
import System.Data.Odbc as ODBCNET
import System.Data.Common as DATACOM



filename = os.path.join(os.getcwd(), 'test.accdb')
print(filename)
if os.path.exists(filename):
    # needs a driver in 32 or 64 bit like your running python
    # https://www.microsoft.com/download/details.aspx?id=13255
    CNXNSTRING = 'Provider=Microsoft.ACE.OLEDB.12.0; Data Source=%s;READONLY=FALSE' % filename
    cnxn = ADONET.OleDbConnection(CNXNSTRING)
    cnxn.Open()
    
    command = cnxn.CreateCommand()
    command.CommandText = "select * from users"
    # command.CommandText = 'select id, name from people where group_id = @group_id'
    # command.Parameters.Add(SqlParameter('group_id', 23))
    rows = command.ExecuteReader()
    print ([rows.GetName(i) for i in range(rows.FieldCount)])
    for  row in rows:
        print([row[i] for i in range(rows.FieldCount)])
    command.Dispose()
    cnxn.Close()
