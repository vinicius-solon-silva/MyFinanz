from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, BigInteger, String, Date, ForeignKey, Boolean, Float
from sqlalchemy.orm import sessionmaker, relationship
from AUTH import CONN_STR


def gera_despesa(descricao, categoria, quantia, data, pago):

    engine = create_engine(CONN_STR, echo=False)
    Sessions = sessionmaker(bind=engine)
    session = Sessions()
    Base = declarative_base()


    class Despesa(Base):
        __tablename__ = 'despesa'

        Descricao = Column(String(255))
        Categoria = Column(String(255))
        Quantia = Column(float)
        Data_Vencimento = Column(String(255))
        Pago = Column(Boolean)

        
    Base.metadata.create_all(engine)
    mfDesp = Despesa(Decricao=descricao, Categoria=categoria, Quantia=quantia, Data_Vencimento=data,Pago=pago)
    session.add(mfDesp)
    session.commit()
    session.close()
    success = "Despesa gerada com sucesso!"

    return success