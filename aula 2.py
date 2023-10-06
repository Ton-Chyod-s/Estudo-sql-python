from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, select, update, delete, ForeignKey, Column
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from asyncio import run

url_do_branco = 'sqlite+aiosqlite:///db.db'

engine = create_async_engine(url_do_branco)

session = sessionmaker(
    engine,
    expire_on_commit = False,
    future = True,
    class_ = AsyncSession,
)

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoa'

    id =  Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)
    posts = relationship('Post', backref='autor')

    def __repr__(self):
        return f'None: {self.nome} Email: {self.email}'
    
class Post(Base):
    __tablename__ = 'post'

    id =  Column(Integer, primary_key=True)
    titulo = Column(String)
    conteudo = Column(String)
    autor_id = Column(Integer, ForeignKey('pessoa.id'))

    def __repr__(self):
        return f'Titulo: {self.titulo} Conteudo: {self.conteudo}'
    
async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def criar_pessoa(nome, email):
    async with session() as s:
        pessoa = (Pessoa(nome=nome, email=email))
        s.add(pessoa)
        post = Post(titulo ='coisa loca isso', conteudo='umas hora ae', pessoa = autor_id)
        s.add(post)
        await s.commit()

async def buscar_pessoa(nome='klayton'):
    async with session() as s:
        query = await s.execute(
            select(Pessoa).where(Pessoa.nome == nome)
        )
        result = query.scalars().all()
        #result = query.all()
        return result

async def atualizar_nome(nome_antigo, none_novo):
    async with session() as s:
        query = await s.execute(
            update(Pessoa).where(Pessoa.nome == nome_antigo).values(nome=none_novo)
        )
        await s.commit()

async def deletar_pessoa(nome):
    async with session() as s:
        query = await s.execute(
            delete(Pessoa).where(Pessoa.nome == nome)
        )
        await s.commit()

#run(create_database())
run(criar_pessoa('lol','lol@gmail.com'))
#print(run(buscar_pessoa()))
#run(atualizar_nome('joão','gabriel'))
#run(deletar_pessoa('gabriel'))