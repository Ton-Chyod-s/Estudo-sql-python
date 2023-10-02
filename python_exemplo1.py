from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Especifique a codificação 'utf-8' na URL de conexão
engine = create_engine('postgresql://postgres:123@localhost:5432/erp?client_encoding=utf8')

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Produto(Base):
    __tablename__ = 'produtos'

    prod_codigo = Column(Integer, primary_key=True)
    prod_descricao = Column(String, nullable=False)
    prod_codbarras = Column(Integer, nullable=False)

    def __repr__(self):
        return f'Produto (descrição={self.prod_descricao}, cod Barras = {self.prod_codbarras})'

data = session.query(Produto).all()
for produto in data:
    print(produto)
