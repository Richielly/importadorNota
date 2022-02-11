# import MySQLdb # para o MySQL
# import sqlite  # para o SQLite
import psycopg2 # para o PostgreSQL
import fdb # para Interbase / Firebird
# import pymssql  #para o MS-SQL. (existem outros módulos - ADOdb for Python/PHP)
# import cx_Oracle #para o Oracle

hostdborigin = 'localhost'
dborigin = 'C:\\Users\\richielly.carvalho\Desktop\SCP_ALMOX\\004\\EQUIPLANO.FDB'
userdborigin = 'sysdba'
senhadborigin = 'masterkey'
portdborigin = 3050

class BdConnections:

    def __init__(self, host='localhost', port=3050, bd_name='C:\\Users\\richielly.carvalho\\Desktop\\324\\equiplano.fdb', user='sysdba', password='masterkey'):
        self.host = host
        self.port = port
        self.bd_name = bd_name
        self.user = user
        self.password = password

    def postgre_connection(self):

        conect = BdConnections()

        con = psycopg2.connect(host=conect.host,
                    port=conect.port,
                    dbname=conect.bd_name,
                    user=conect.user,
                    password=conect.password)
        return con

    def firebird_connection(self):

        conect = BdConnections()

        conn = fdb.connect(host=conect.host, database=conect.bd_name,
                          user=conect.user,
                          password=conect.password,
                          port=conect.port)
        return conn

    def mysql_connection(self,host, bd, user, password):
        con = MySQLdb.connect(host, user, password)
        con.select_db(bd)

    def sqlite_connection(self, bd):
        con = sqlite.connect(bd, mode=775)

    def mssql_connection(self, host, database, user, password):
        con = pymssql.connect(host = host,
                      user = user,
                      password = password,
                      database = database)
