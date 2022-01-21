import pandas as pd
import sqlalchemy
import psycopg2 # para o PostgreSQL

banco = 'postgresql+psycopg2://NotaCasteloBranco:es74079@localhost/NotaCasteloBranco'
sheet = "C:\\Users\\richielly.carvalho\\Desktop\\NotaCasteloBranco\\ArquivosConcorrentes\\Notas Fiscais Canceladas.csv"

engine = sqlalchemy.create_engine(banco)

df = pd.read_csv(sheet, encoding = 'latin1')

df.to_sql(
    name = 'nota_cancelada',
    con = engine,
    index = False
    #if_exists ='append' Utilizar se quiser incluir dados replicados no banco existente
)

