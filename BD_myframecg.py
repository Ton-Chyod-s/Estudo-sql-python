from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import String, Integer, select, update, delete, ForeignKey, Column, Float
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from asyncio import run
import bd

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
    nome = Column(String(80), nullable=True)
    e_mail = Column(String(50), nullable=True)
    whats_app = Column(String(15), nullable=True)
    localidade = Column(String(30), nullable=True) 
    posts = relationship('Venda', backref='cliente')

    def __repr__(self):
        return f'None: {self.nome} Email: {self.email}'
    
class Venda(Base):
    __tablename__ = 'venda'

    id =  Column(Integer, primary_key=True)
    produto = Column(String(50), nullable=True)
    qtde = Column(Integer, nullable=True)
    valor = Column(String(5), nullable=True)
    data_pedido = Column(String(10), nullable=True)
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    autor = relationship('Cliente', backref='venda')

    def __repr__(self):
        return f'Produto: {self.produto} Quantidade: {self.qtde} Valor: {self.valor} Data pedido: {self.data_pedido}'
    
class Despesavenda(Base):
    __tablename__ = 'despesas_vendas'

    id =  Column(Integer, primary_key=True)
    uber_flash = Column(String(5), nullable=False)
    impressao = Column(String(5), nullable=False)
    outros = Column(String(5), nullable=False)
    venda_id = Column(Integer, ForeignKey('venda.id'))
    venda = relationship('Venda', backref='despesas_vendas')

    def __repr__(self):
        return f'Uber flash: {self.uber_flash} Impressão: {self.impressao} Outros: {self.outros}'
    
class Estoque(Base):
    __tablename__ = 'estoque'

    id =  Column(Integer, primary_key=True)
    fornecedor = Column(String(50), nullable=True)
    produto = Column(String(50), nullable=True)
    qtde = Column(Integer, nullable=True)
    valor = Column(String(10), nullable=True)
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

for i in bd.estoque_2023:
    linha = i.split(",")
    lol = linha[3].replace(".",",")
    run(estoque(linha[0],linha[1],linha[2],lol,linha[4]))

#run(venda_realizada('nome','email', 'telefone','localidade','quadro descrição', 'quantidade', 'valor','data venda','uber flash','impressão','outros'))

for linha in bd.venda_2023:
    linha = linha.split(",")
    valor = linha[6].replace(".",",")
    nome = linha[0]
    email = linha[1]
    telefone = linha[2]
    localidade = linha[3]
    quadro_descricao = linha[4]
    quantidade = linha[5]
    data_venda = linha[7].replace("yyyy","2023")
    if float(linha[8]) > 0:
        uber_flash = linha[8].replace(".",",")
    else:
        uber_flash = '0'
    try:
        impressao = linha[9]
    except:
        impressao = '0'
    
    run(venda_realizada(linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], valor, data_venda, uber_flash, impressao,'0'))