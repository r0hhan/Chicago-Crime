import cx_Oracle
from app import app

deets = 'rwanare/'+app.config['PASSWORD']+'@oracle.cise.ufl.edu:1521/orcl'
conn = cx_Oracle.connect(deets)
print (conn.version)
conn.close()
