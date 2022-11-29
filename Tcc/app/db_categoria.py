from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, BigInteger, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from AUTH import CONN_STR


def gera_categoria(nome,descricao):

    engine = create_engine(CONN_STR, echo=False)
    Sessions = sessionmaker(bind=engine)
    session = Sessions()
    Base = declarative_base()


    class Categoria(Base):
        __tablename__ = 'categoria'

        Nome = Column(String(255))
        Descricao = Column(String(255))

        
    Base.metadata.create_all(engine)
    mfCateg = Categoria(Nome=nome, Decricao=descricao)
    session.add(mfCateg)
    session.commit()
    session.close()
    success = "Categoria gerada com sucesso!"

    return success