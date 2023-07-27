import sqlalchemy 
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

#conectando ao banco de dados
engine = sqlalchemy.create_engine('sqlite:///mysql_alchemy.db', echo=True)

#criar sessão
Session = sessionmaker(bind=engine)
session = Session()

#declarando o mapeamento
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    age = Column(Integer)

    def __repr__(self):
        return "<User(name={}, fullname={}, age={})>".format(
            self.firstname, self.lastname, self.age)

nome = str(input('None:\t')).upper()
sobrenome = str(input('Sobrenome:\t')).upper()
idade = int(input('Idade:\t'))

# Consultar todos os usuários no banco de dados e imprimir suas informações
user = session.query(User).filter_by(firstname=nome).first()
if user is None:
    novo = User(firstname=nome,lastname= sobrenome, age=idade)
    session.add(novo)
    session.commit()
    print('Adicionado com sucesso!')
else:
    print('Nome existente!')


"""
# Consultar o usuário com o ID igual a 1
user_to_delete = session.query(User).filter_by(id=3).first()
session.delete(user_to_delete)
session.commit()

#criar tabela banco de dados
Base.metadata.create_all(engine)

#adicionando informações ao banco de dados
session.add_all([
    User(firstname='FRANCISCO',lastname= 'ENZO', age=20),
    User(firstname='MARIA',lastname= 'VALENTINA', age=23),
    User(firstname='JOÃO',lastname= 'PEDRO', age=22)
])

session.commit()

users = session.query(User).all()
for user in users:
    print(user)"""

"""#consultar objetos (select)
query_user = session.query(User).filter_by(name='valentina').first()
print(query_user) #.fullname

#consultar todos os usuarios no banco de dados
for info in session.query(User.name, User.age).order_by(User.id):
    print(info)"""


