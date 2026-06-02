# pip install sqlalchemy pymysql
# pip install python-dotenv

from sqlalchemy import create_engine
# necessário para trabalhar com .env
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

host = os.getenv('db_host')
user = os.getenv('db_user')
password = os.getenv('db_password')
database = os.getenv('db_database')


engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}/{database}'
)

try:
    df_clientes = pd.read_sql('tb_clientes', engine)
    df_itens = pd.read_sql('tb_itens', engine)
    df_pedidos = pd.read_sql('tb_pedidos', engine)
    df_peodutos = pd.read_sql('tb_produtos', engine)

    print(df_pedidos.head(5))

except Exception as e:
    print(f'Falha na conexão {e}')



# Merge: juntar dois dataframes:
    df_merge1 = pd.merge(
        df_clientes, df_pedidos, on='codigo_produto'
    )

# Merge: quando os nomes das colunas são diferentes é necessário ingormar o 
    df_merge1 = pd.merge(
        df_pedidos, 
    )




# ==================================================================================
    
# pip install python-dotenv



