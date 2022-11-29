from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, BigInteger, String, Date, ForeignKey, Boolean, Float
from sqlalchemy.orm import sessionmaker, relationship
from AUTH import CONN_STR


def gera_receita(descricao, categoria, quantia, data):

    engine = create_engine(CONN_STR, echo=False)
    Sessions = sessionmaker(bind=engine)
    session = Sessions()
    Base = declarative_base()


    class Receita(Base):
        __tablename__ = 'receita'

        Descricao = Column(String(255))
        Categoria = Column(String(255))
        Quantia = Column(float)
        Data_Recebida = Column(String(255))

        
    Base.metadata.create_all(engine)
    mfReceita = Receita(Decricao=descricao, Categoria=categoria, Quantia=quantia, Data_Recebida=data)
    session.add(mfReceita)
    session.commit()
    session.close()
    success = "Receita gerada com sucesso!"

    return success