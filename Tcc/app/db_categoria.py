from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, BigInteger, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from AUTH import CONN_STR

def gera_categoria(nome, limite):

    engine = create_engine(CONN_STR, echo=False)
    Sessions = sessionmaker(bind=engine)
    session = Sessions()
    Base = declarative_base()


    class Categoria(Base):
        __tablename__ = 'categoria'

        Nome = Column(String(255), primary_key = True)
        Limite = Column(BigInteger)


    try:    
        Base.metadata.create_all(engine)
        mfCateg = Categoria(Nome=nome, Limite=limite)
        session.add(mfCateg)
        session.commit()
        session.close()
        success = "Categoria gerada com sucesso!"
    except:
        success = 'Algo deu errado... Verifique as informações!'

    return str(success)