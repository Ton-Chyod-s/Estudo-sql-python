from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import String, Integer, select, update, delete, ForeignKey, Column, Float
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from asyncio import run
import bd
import time

#conectar/criar banco de dados
url_do_branco = 'sqlite+aiosqlite:///myframecg.db'
#criando conecção asincrona com bando de dados
engine = create_async_engine(url_do_branco)

session = sessionmaker(
    engine,
    expire_on_commit = False,
    future = True,
    #se não declara a sessão é sincrona
    class_ = AsyncSession,
)

Base = declarative_base()
#tabela de clientes 
class Cliente(Base):
    __tablename__ = 'cliente'
    #coluna da tabela
    id =  Column(Integer, primary_key=True)
    nome = Column(String(80), nullable=False)
    e_mail = Column(String(50))
    whats_app = Column(String(15), nullable=False)
    localidade = Column(String(30), nullable=False) 
    posts = relationship('Venda', backref='cliente')
    #modo grafico de representação
    def __repr__(self):
        return f'id:{self.id},nome:{self.nome},e-mail:{self.e_mail},whats-app:{self.whats_app},localidade:{self.localidade}'
#tabela de venda    
class Venda(Base):
    __tablename__ = 'venda'
    #coluna da tabela
    id =  Column(Integer, primary_key=True)
    produto = Column(String(50), nullable=False)
    qtde = Column(Integer, nullable=False)
    valor = Column(String(5), nullable=False)
    data_pedido = Column(String(10), nullable=False)
    status = Column(String(50))
    cliente_id = Column(Integer, ForeignKey('cliente.id'))
    autor = relationship('Cliente', backref='venda')
    #modo grafico de representação
    def __repr__(self):
        return f'ID vendas,{self.id},Produto,{self.produto},Quantidade,{self.qtde},Valor,{self.valor},Data pedido,{self.data_pedido},id,{self.cliente_id},status,{self.status}'
#tabela de despesas vendas    
class Despesavenda(Base):
    __tablename__ = 'despesas_vendas'
    #coluna da tabela
    id =  Column(Integer, primary_key=True)
    uber_flash = Column(String(5))
    impressao = Column(String(5), nullable=False)
    outros = Column(String(5))
    venda_id = Column(Integer, ForeignKey('venda.id'))
    venda = relationship('Venda', backref='despesas_vendas')
    #modo grafico de representação
    def __repr__(self):
        return f'Uber flash:{self.uber_flash}:Impressão:{self.impressao}:Outros:{self.outros}:Venda ID:{self.venda_id}'
#tabela estoque    
class Estoque(Base):
    __tablename__ = 'estoque'
    #coluna da tabela
    id =  Column(Integer, primary_key=True)
    fornecedor = Column(String(50), nullable=True)
    produto = Column(String(50), nullable=True)
    qtde = Column(Integer, nullable=True)
    valor = Column(String(10), nullable=True)
    data_pedido = Column(String, nullable=True)
    ecomerce = Column(String, nullable=True)
    #modo grafico de representação
    def __repr__(self):
        return f'id.{self.id}.Fornecedor.{self.fornecedor}.Produto.{self.produto}.Quantidade.{self.qtde}.Valor.{self.valor}.Data pedido.{self.data_pedido}.E-commerce.{self.ecomerce}'
#tabela DRE
class Dre(Base):
    __tablename__ = 'dre'
    #coluna da tabela
    id =  Column(Integer, primary_key=True)
    descricao = Column(String(50), nullable=True)
    def __repr__(self):
        return f'Descrição:{self.descricao}'
    
#função para criar banco de dadps 
async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def inserir_dre(descricao):
    async with session() as s:
        pessoa = (Dre(descricao=descricao))
        s.add(pessoa)
        await s.commit()

async def venda_realizada(nome, email, whats_app, localidade, produto, quantidade, valor, data_pedido, uber_flash, impressao, outros,status):
    async with session() as s:
        pessoa = (Cliente(nome=nome, e_mail=email, whats_app = whats_app, localidade = localidade))
        s.add(pessoa)
        venda = Venda(produto=produto, qtde=quantidade, valor=valor, data_pedido=data_pedido,status=status, cliente=pessoa)
        s.add(venda)
        despesas_venda = Despesavenda(uber_flash=uber_flash, impressao=impressao, outros=outros, venda=venda)
        s.add(despesas_venda)
        await s.commit()
    
async def estoque(fornecedor, produto, qtde, valor, data_pedido, ecomerce):
    async with session() as s:
        estoque = (Estoque(fornecedor=fornecedor, produto=produto, qtde = qtde, valor = valor,data_pedido=data_pedido, ecomerce = ecomerce))
        s.add(estoque)
        await s.commit()
    
async def buscar_pessoa(nome):
    async with session() as s:
        query = await s.execute(
            select(Cliente).where(Cliente.nome == nome)
        )
        result = query.scalars().all()
        #result = query.all()
        return result

async def buscar_id_venda(id):
    async with session() as s:
        query = await s.execute(
            select(Venda).where(Venda.cliente_id == id)
        )
        result = query.scalars().all()
        #result = query.all()
        return result

async def buscar_id_despesas(id):
    async with session() as s:
        query = await s.execute(
            select(Despesavenda).where(Despesavenda.venda_id == id)
        )
        result = query.scalars().all()
        #result = query.all()
        return result

async def buscar_fornecedor(nome):
    async with session() as s:
        query = await s.execute(
            select(Estoque).where(Estoque.fornecedor == nome)
        )
        result = query.scalars().all()
        #result = query.all()
        return result

async def atualizar_cliente_nome(dado_antigo, dado_novo):
    async with session() as s:
        query = await s.execute(
            update(Cliente).where(Cliente.nome == dado_antigo).values(nome=dado_novo)
        )
        await s.commit()

async def atualizar_cliente_e_mail(dado_antigo, dado_novo):
    async with session() as s:
        query = await s.execute(
            update(Cliente).where(Cliente.e_mail == dado_antigo).values(e_mail=dado_novo)
        )
        await s.commit()

async def atualizar_cliente_whats_app(dado_antigo, dado_novo):
    async with session() as s:
        query = await s.execute(
            update(Cliente).where(Cliente.whats_app == dado_antigo).values(whats_app=dado_novo)
        )
        await s.commit()

async def atualizar_cliente_localidade(dado_antigo, dado_novo):
    async with session() as s:
        query = await s.execute(
            update(Cliente).where(Cliente.id == dado_antigo).values(localidade=dado_novo)
        )
        await s.commit()

async def atualizar_venda_produto(dado_antigo, dado_novo):
    async with session() as s:
        query = await s.execute(
            update(Venda).where(Venda.produto == dado_antigo).values(produto=dado_novo)
        )
        await s.commit()

async def atualizar_venda_qtde(dado_antigo, dado_novo):
    async with session() as s:
        query = await s.execute(
            update(Venda).where(Venda.qtde == dado_antigo).values(qtde=dado_novo)
        )
        await s.commit()

async def atualizar_venda_valor(dado_antigo, dado_novo):
    async with session() as s:
        query = await s.execute(
            update(Venda).where(Venda.valor == dado_antigo).values(valor=dado_novo)
        )
        await s.commit()

async def atualizar_venda_data_pedido(dado_antigo, dado_novo):
    async with session() as s:
        query = await s.execute(
            update(Venda).where(Venda.data_pedido == dado_antigo).values(data_pedido=dado_novo)
        )
        await s.commit()

async def atualizar_venda_status(dado_antigo, dado_novo):
    async with session() as s:
        query = await s.execute(
            update(Venda).where(Venda.status == dado_antigo).values(status=dado_novo)
        )
        await s.commit()

async def atualizar_despesasvenda_uber_flash(dado_antigo, dado_novo):
    async with session() as s:
        query = await s.execute(
            update(Despesavenda).where(Despesavenda.venda_id == dado_antigo).values(uber_flash=dado_novo)
        )
        await s.commit()

async def atualizar_despesasvenda_impressao(dado_antigo, dado_novo):
    async with session() as s:
        query = await s.execute(
            update(Despesavenda).where(Despesavenda.impressao == dado_antigo).values(impressao=dado_novo)
        )
        await s.commit()

async def atualizar_despesasvenda_outros(dado_antigo, dado_novo):
    async with session() as s:
        query = await s.execute(
            update(Despesavenda).where(Despesavenda.venda_id == dado_antigo).values(outros=dado_novo)
        )
        await s.commit()

async def atualizar_estoque_produto(dado_antigo, dado_novo):
    async with session() as s:
        query = await s.execute(
            update(Estoque).where(Estoque.produto == dado_antigo).values(produto=dado_novo)
        )
        await s.commit()

async def atualizar_estoque_qtde(dado_antigo, dado_novo):
    async with session() as s:
        query = await s.execute(
            update(Estoque).where(Estoque.id == dado_antigo).values(qtde=dado_novo)
        )
        await s.commit()

async def atualizar_estoque_valor(dado_antigo, dado_novo):
    async with session() as s:
        query = await s.execute(
            update(Estoque).where(Estoque.valor == dado_antigo).values(valor=dado_novo)
        )
        await s.commit()

async def atualizar_estoque_data_pedido(dado_antigo, dado_novo):
    async with session() as s:
        query = await s.execute(
            update(Estoque).where(Estoque.data_pedido == dado_antigo).values(data_pedido=dado_novo)
        )
        await s.commit()

async def atualizar_estoque_ecomerce(dado_antigo, dado_novo):
    async with session() as s:
        query = await s.execute(
            update(Estoque).where(Estoque.ecomerce == dado_antigo).values(ecomerce=dado_novo)
        )
        await s.commit()

async def atualizar_estoque_fornecedor(dado_antigo, dado_novo):
    async with session() as s:
        query = await s.execute(
            update(Estoque).where(Estoque.fornecedor == dado_antigo).values(fornecedor=dado_novo)
        )
        await s.commit()

async def deletar_pessoa(nome):
    async with session() as s:
        query = await s.execute(
            delete(Cliente).where(Cliente.nome == nome)
        )
        await s.commit()

async def deletar_venda(nome):
    async with session() as s:
        query = await s.execute(
            delete(Venda).where(Venda.cliente_id == nome)
        )
        await s.commit()

async def deletar_despesasvenda(nome):
    async with session() as s:
        query = await s.execute(
            delete(Despesavenda).where(Despesavenda.venda_id == nome)
        )
        await s.commit()

async def deletar_linha_estoque(nome):
    async with session() as s:
        query = await s.execute(
            delete(Estoque).where(Estoque.fornecedor == nome)
        )
        await s.commit()

async def ler_planilha(txt):
    async with session() as s:
        query = await s.execute(
            select(txt)
        )
        result = query.scalars().all()
        #result = query.all()
        return result

def despesa_venda():
    return run(ler_planilha(Despesavenda))

def venda ():
    return run(ler_planilha(Venda))

def clientes():
    return run(ler_planilha(Cliente))

def estoque_():
    return run(ler_planilha(Estoque))

def dre_():
    return run(ler_planilha(Dre))


if __name__ == '__main__':
    run(create_database())

   #adicionar informações no banco de dados estoque
    for i in bd.estoque_2023:
        linha = i.split(".")
        nome_loja = linha[0]
        produto = linha[1]
        quantidade = linha[2]
        valor = f'{linha[3]},{linha[4]}'
        data = linha[5]
        ecommerce = linha[6]

        run(estoque(nome_loja,produto,quantidade,valor,data,ecommerce))

    #adicionar informações no banco de dados venda
    for linha in bd.venda_2023:
        linha = linha.split(",")
        valor = linha[6]
        nome = linha[0]
        email = linha[1]
        telefone = linha[2]
        localidade = linha[3]
        quadro_descricao = linha[4]
        quantidade = linha[5]
        data_venda = linha[7]
        uber_flash = linha[8]
        impressao = linha[9]
        outros = '0'
        status = linha[10]

        run(venda_realizada(nome,email,telefone,localidade,quadro_descricao,quantidade,valor,data_venda,uber_flash,impressao,outros,status))

    #adicionar informações no banco de dados dre
    for i in bd.dre_2023:
        run(inserir_dre(i))