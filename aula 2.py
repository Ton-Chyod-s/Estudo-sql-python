from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import String, Integer, select, update, delete, ForeignKey, Column, Float
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from asyncio import run

url_do_branco = 'sqlite+aiosqlite:///myframecg.db'

engine = create_async_engine(url_do_branco)

session = sessionmaker(
    engine,
    expire_on_commit = False,
    future = True,
    class_ = AsyncSession,
)

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'cliente'

    id =  Column(Integer, primary_key=True)
    nome = Column(String)
    e_mail = Column(String)
    whats_app = Column(String, nullable=True)
    localidade = Column(String) 
    posts = relationship('Venda', backref='cliente')

    def __repr__(self):
        return f'None: {self.nome} Email: {self.email}'
    
class Venda(Base):
    __tablename__ = 'venda'

    id =  Column(Integer, primary_key=True)
    produto = Column(String)
    qtde = Column(Integer)
    valor = Column(String)
    data_pedido = Column(String, nullable=True)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    autor = relationship('Cliente', backref='venda')

class Despesavenda(Base):
    __tablename__ = 'despesas_vendas'

    id =  Column(Integer, primary_key=True)
    uber_flash = Column(String)
    impressao = Column(Integer)
    outros = Column(String)
    venda_id = Column(Integer, ForeignKey('venda.id'))
    venda = relationship('Venda', backref='despesas_vendas')

    def __repr__(self):
        return f'Uber flash: {self.uber_flash} Impressão: {self.impressao} Outros: {self.outros}'
    
class Estoque(Base):
    __tablename__ = 'estoque'

    id =  Column(Integer, primary_key=True)
    fornecedor = Column(String)
    produto = Column(String)
    qtde = Column(Integer)
    valor = Column(String)
    data_pedido = Column(String, nullable=True)
    def __repr__(self):
        return f'Fornecedor: {self.fornecedor} Produto: {self.produto} Quantidade: {self.qtde} Valor: {self.valor} Data pedido: {self.data_pedido}'
    
async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
   
async def venda_realizada(nome, email, whats_app, localidade, produto, quantidade, valor, data_pedido, uber_flash, impressao, outros):
    async with session() as s:
        pessoa = (Cliente(nome=nome, e_mail=email, whats_app = whats_app, localidade = localidade))
        s.add(pessoa)
        venda = Venda(produto=produto, qtde=quantidade, valor=valor, data_pedido=data_pedido, cliente=pessoa)
        s.add(venda)
        despesas_venda = Despesavenda(uber_flash=uber_flash, impressao=impressao, outros=outros, venda=venda)
        s.add(despesas_venda)
        await s.commit()
    
async def estoque(fornecedor, produto, qtde, valor, data_pedido):
    async with session() as s:
        estoque = (Estoque(fornecedor=fornecedor, produto=produto, qtde = qtde, valor = valor,data_pedido=data_pedido))
        s.add(estoque)
        await s.commit()
    
async def buscar_pessoa(nome='klayton'):
    async with session() as s:
        query = await s.execute(
            select(Cliente).where(Cliente.nome == nome)
        )
        result = query.scalars().all()
        #result = query.all()
        return result

async def atualizar_nome(nome_antigo, none_novo):
    async with session() as s:
        query = await s.execute(
            update(Cliente).where(Cliente.nome == nome_antigo).values(nome=none_novo)
        )
        await s.commit()

async def deletar_pessoa(nome):
    async with session() as s:
        query = await s.execute(
            delete(Cliente).where(Cliente.nome == nome)
        )
        await s.commit()

run(create_database())
#run(venda_realizada('klayton','arqkdias@gmail.com', '67991799956','campo grande','20x25', 1, '65.00','09/10/2023'))
run(estoque('BRANDÃO MOLDURAS','20X25',5,'78.00','09/10/2023'))
#run(venda_realizada('nome','email', 'telefone','localidade','quadro', 'quantidade', 'valor','data venda','uber flash','impressão','outros'))
run(venda_realizada('klayton','arqkdias@gmail.com', '67991799956','campo grande','20x25', 1, '65.00','09/10/2023','5.85','1,85','0'))