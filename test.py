from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column
from sqlalchemy import String, select
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

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))

    def __repr__(self):
        return f'None: {self.nome} Email: {self.email}'
    
async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def criar_pessoa(nome, email):
    async with session() as s:
        s.add(Pessoa(nome=nome, email=email))
        await s.commit()

async def buscar_pessoa(nome):
    async with session() as s:
        query = await s.execute(
            select(Pessoa).where(Pessoa.nome == nome)
        )


#run(create_database())
run(criar_pessoa('klayton','arqkdias@gmail.com'))
