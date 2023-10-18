from sqlalchemy import create_engine, text, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Numeric
from sqlalchemy.orm import sessionmaker

# Config
connection_url = "postgresql://postgres:123@localhost:5432/myframe"
engine = create_engine(connection_url, echo=True)

conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

metadata = MetaData(bind=engine)

dre_table = Table('dre', metadata, autoload=True)

'''# Executando a consulta
result = conn.execute(text('SELECT * FROM dre'))

# Exibindo os nomes das colunas
for linha in result:
    descricao = linha[2]
    print(descricao)'''


# Entidades
class Frame(Base):
    __tablename__ = "dre"

    def __repr__(self):
        return f"{self.id} | {self.descricao} | {self.conta} | {self.tipo} | " 

data = session.query(Frame).all()
print(data[2])

'''
#insert
data_insert = Frame(name="edi-marley")
session.add(data_insert)
session.commit()

#delete
session.query(Frame).filter(Frame.name == "klayton").delete()
session.commit()


#update
session.query(Frame).filter(Frame.name == "edi-marley").update({"name": "klayton"})
session.commit()

#select
data = session.query(Frame).all()
print(data)
print(data[0].name)
print(data[1].name)


session.close()
'''