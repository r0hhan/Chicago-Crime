import cx_Oracle
from pprint import pprint
from app import app

def getAll():
    connector = 'rwanare/'+app.config['PASSWORD']+'@oracle.cise.ufl.edu:1521/orcl'
    con = cx_Oracle.connect(connector)
    cur = con.cursor()
    cur.execute("SELECT COUNT(*) FROM crime")
    for x in cur:
        return (x[0])
        break
    con.close()
