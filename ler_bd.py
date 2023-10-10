import pandas as pd  
from sqlalchemy import create_engine 


cnx = create_engine('sqlite:///myframecg.db').connect() 
df = pd.read_sql_table('cliente', cnx) 
print(df)
df = pd.read_sql_table('venda', cnx) 
print(df)
df = pd.read_sql_table('despesas_vendas', cnx) 
print(df)