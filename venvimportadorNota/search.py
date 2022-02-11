import connection

class Search():

    def select(self, script):

        conect = connection.BdConnections()

        conn = conect.firebird_connection()
        # conn = conect.postgre_connection()
        cur = conn.cursor()
        cur.execute(script)
        lista = cur.fetchall()
        cur.close()
        conn.close()

        return lista

    def select_tables_firebird(self):
        con = connection.BdConnections()
        conn = con.firebird_connection(host=hostdborigin, database=dborigin, user=userdborigin, password=senhadborigin,
                                       port=portdborigin)
        cur = conn.cursor()
        cur.execute(
            """ select 
                rdb$relation_name from rdb$relations
                where rdb$system_flag = 0; """)
        lista = cur.fetchall()
        cur.close()
        conn.close()

        return lista

    def select_columns_firebird(self, table_name):
        con = connection.BdConnections()

        conn = con.firebird_connection(host=hostdborigin, database=dborigin, user=userdborigin, password=senhadborigin,
                                       port=portdborigin)
        cur = conn.cursor()
        cur.execute(
            """ select rdb$field_name from rdb$relation_fields
             where rdb$relation_name=""" + "'" + table_name + "'" + ';')
        lista = cur.fetchall()
        cur.close()
        conn.close()

        return lista

    def select_filter_firebird(self, table, column='*'):
        con = connection.BdConnections()
        conn = con.firebird_connection(host=hostdborigin, database=dborigin, user=userdborigin, password=senhadborigin,
                                       port=portdborigin)
        cur = conn.cursor()
        cur.execute(
            """ SELECT """
            + column +
            """ FROM """ + table + ";")
        lista = cur.fetchall()
        cur.close()
        conn.close()

        return lista

    def select_postgre(self):
        con = connection.BdConnections()
        conn = con.postgre_connection(host=hostdest, port=portdest, bd=bddest, user=userdest, password=passworddest)
        cur = conn.cursor()
        cur.execute(
            """ SELECT idconfiguracao, idcliente, estado, idusuariocriador, datacriacao, idusuarioatualizador, dataatualizacao, chaveacesso, quantidadelinhastabelas, diferencaordemretirada, tamanhomaximoanexo, conferenciacega, localbkp, dataultimobkp, diabackup
	FROM public.configuracao; """)
        lista = cur.fetchall()
        cur.close()
        conn.close()

        return lista

    def select_tables_postgre(self):
        con = connection.BdConnections()
        conn = con.postgre_connection(host=hostdest, port=portdest, bd=bddest, user=userdest, password=passworddest)
        cur = conn.cursor()
        cur.execute(
            """SELECT table_name 
               FROM information_schema.tables
               WHERE table_schema='public'
               AND table_type='BASE TABLE';""")

        list = cur.fetchall()
        cur.close()
        conn.close()

        return list

    def select_columns_tables(self, table_name):
        con = connection.BdConnections()
        conn = con.postgre_connection(host=hostdest, port=portdest, bd=bddest, user=userdest, password=passworddest)
        cur = conn.cursor()
        cur.execute(
            """SELECT column_name, data_type, character_maximum_length
               FROM INFORMATION_SCHEMA.COLUMNS 
               WHERE table_name = """ + "'" + table_name + "'" + ';')

        list = cur.fetchall()
        cur.close()
        conn.close()

        return list

    def select_filter(self, table, column='*'):
        con = connection.BdConnections()
        conn = con.postgre_connection(host=hostdest, port=portdest, bd=bddest, user=userdest, password=passworddest)
        cur = conn.cursor()
        cur.execute(
            """ SELECT """
            + column +
            """ FROM public. """ + table + ";")
        lista = cur.fetchall()
        cur.close()
        conn.close()

        return lista