import connection
_schema = 'bethadba'



def minenar(consulta, like):
    if(like):
        _like_init = """ like upper('%"""
        _like_finish = """%')"""
    else:
        _like_init = """=upper('"""
        _like_finish = """') """

    _resultado = []
    _tabela = []
    _coluna = []
    conn = connection.BdConnections(port=5432, bd_name='FrotasUniflor',user='FrotasUniflor', password='es74079')

    cur = conn.postgre_connection()
    cur = cur.cursor()

    # encontrando as colunas do banco
    cur.execute(f''' select table_name FROM information_schema.tables WHERE table_schema='{_schema}' ''')
    tabelas = cur.fetchall()
    # encontrando as colunas do banco
    for tabela in tabelas:
        cur.execute(f''' SELECT column_name, data_type from information_schema.columns WHERE table_name ='{tabela[0]}' ''')
        colunas = cur.fetchall()

        for coluna in colunas:
            try:
                if (coluna[1] == 'character' or coluna[1] == 'character varying' or coluna[1] == 'text'):
                    # cur.execute(f''' select * from bethadba.{tabela[0]} a where upper(a.{coluna[0]})=upper('{consulta}') ''')
                    cur.execute(f''' select * from bethadba.{tabela[0]} a where upper(a.{coluna[0]}){_like_init}{consulta}{_like_finish} ''')
                    # print(f''' select * from bethadba.{tabela[0]} a where upper(a.{coluna[0]}){_like_init}{consulta}{_like_finish} ''')
                    resultados = cur.fetchall()
                    for resultado in resultados:
                        if(len(resultado) > 0):
                            _tabela.append(tabela[0])
                            _resultado.append(resultado)
            except : 'Tabela não ecnontrada'

    consulta = ''
    cur.close()
    return _tabela, _resultado

def colunas(coluna,like):

    _tabelas = []

    if (like):
        _like_init = """ like upper('%"""
        _like_finish = """%')"""
    else:
        _like_init = """=upper('"""
        _like_finish = """') """

    conn = connection.BdConnections(port=5432, bd_name='FrotasUniflor', user='FrotasUniflor', password='es74079')
    cur = conn.postgre_connection()
    cur = cur.cursor()

    # encontrando as tabelas do banco
    cur.execute(f''' select table_name FROM information_schema.tables WHERE table_schema='{_schema}' ''')
    tabelas = cur.fetchall()

    # encontrando as colunas do banco
    for tabela in tabelas:
        # cur.execute(f''' SELECT column_name, data_type from information_schema.columns WHERE table_name ='{tabela[0]}' ''')
        cur.execute(f''' SELECT column_name, data_type from information_schema.columns WHERE table_name ='{tabela[0]}' ''')
        colunas = cur.fetchall()

        for col in colunas:
            if col[0] == coluna:
                _tabelas.append(tabela)
    cur.close()
    return _tabelas