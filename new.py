from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import sessionmaker

# Config
connection_url = "postgresql://postgres:123@localhost:5432/myframe"
engine = create_engine(connection_url, echo=True)
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Entidades
class Frame(Base):
    __tablename__ = "myframe"
    name = Column(String, primary_key=True)

    def __repr__(self):
        return f"Cliente (name={self.name})"

"""#insert
data_insert = Frame(name="edi-marley")
session.add(data_insert)
session.commit()

#delete
session.query(Frame).filter(Frame.name == "klayton").delete()
session.commit()
"""

#update
session.query(Frame).filter(Frame.name == "edi-marley").update({"name": "klayton"})
session.commit()

#select
data = session.query(Frame).all()
print(data)
print(data[0].name)
print(data[1].name)

session.close()
