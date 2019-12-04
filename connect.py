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

def s1mple1():
    connector = 'rwanare/'+app.config['PASSWORD']+'@oracle.cise.ufl.edu:1521/orcl'
    con = cx_Oracle.connect(connector)
    cur = con.cursor()
    record = []
    cur.execute("SELECT type_of_crime, round(100*(COUNT(*) / SUM(COUNT(*)) OVER ()),2) perc FROM crime GROUP BY type_of_crime")
    for x in cur:
        record.append(x)

    con.close()
    return record

def s1mple2():
    connector = 'rwanare/'+app.config['PASSWORD']+'@oracle.cise.ufl.edu:1521/orcl'
    con = cx_Oracle.connect(connector)
    cur = con.cursor()
    record = []
    cur.execute("SELECT COUNT(*) FROM CRIME WHERE EXTRACT(YEAR FROM date_of_crime) BETWEEN 2001 and 2005")
    for x in cur:
        record.append(x[0])

    cur.execute("SELECT COUNT(*) FROM CRIME WHERE EXTRACT(YEAR FROM date_of_crime) BETWEEN 2006 and 2010")
    for x in cur:
        record.append(x[0])

    cur.execute("SELECT COUNT(*) FROM CRIME WHERE EXTRACT(YEAR FROM date_of_crime) BETWEEN 2011 and 2015")
    for x in cur:
        record.append(x[0])

    cur.execute("SELECT COUNT(*) FROM CRIME WHERE EXTRACT(YEAR FROM date_of_crime) BETWEEN 2016 and 2019")
    for x in cur:
        record.append(x[0])
    return record
    con.close()

def s1mpleTest(year1, year2):
    connector = 'rwanare/'+app.config['PASSWORD']+'@oracle.cise.ufl.edu:1521/orcl'
    con = cx_Oracle.connect(connector)
    cur = con.cursor()
    record = []
    cur.execute("SELECT count(*) from crime where EXTRACT(year from date_of_crime)>='{0}' and EXTRACT(year from date_of_crime)<='{1}'".format(year1, year2))
    for x in cur:
        record.append(x)

    cur.execute("SELECT count(*) from crime where EXTRACT(year from date_of_crime) between 2000 and 2010")
    for x in cur:
        record.append(x)

    return record
    con.close()

#s1mple3 (heat map under construction *bonus query* xd)

def complex2(crime_value):
    connector = 'rwanare/'+app.config['PASSWORD']+'@oracle.cise.ufl.edu:1521/orcl'
    con = cx_Oracle.connect(connector)
    cur = con.cursor()
    record = []
    cur.execute("SELECT EXTRACT(HOUR FROM date_of_crime), COUNT(*) count_crime FROM crime WHERE EXTRACT(YEAR from date_of_crime) BETWEEN 2018 and 2019 AND type_of_crime ='" + crime_value + "' GROUP BY EXTRACT(HOUR FROM date_of_crime) ORDER BY EXTRACT(HOUR FROM date_of_crime)")
    for x in cur:
        record.append(x)

    return record
    con.close()
