import cx_Oracle
from pprint import pprint
from app import app

deets = 'rwanare/'+app.config['PASSWORD']+'@oracle.cise.ufl.edu:1521/orcl'
# conn = cx_Oracle.connect(deets)
# print (conn.version)
# cur = conn.cursor()
# cur.execute("SELECT COUNT(*) FROM crime")
# for x in cur:
#     print (x[0])
# conn.close()
