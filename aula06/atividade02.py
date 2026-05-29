from sqlalchemy import create_engine
import pandas as pd

host = 'localhost'
user = 'root'
password = ''
database = 'bd_atividade02'

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






