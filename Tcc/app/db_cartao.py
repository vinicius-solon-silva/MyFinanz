from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, BigInteger, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from AUTH import CONN_STR

def cadastrar_cartao(nome, cpf, numCartao, data, tipo):

    cpf = int(cpf)

    engine = create_engine(CONN_STR, echo=False)
    Sessions = sessionmaker(bind=engine)
    session = Sessions()
    Base = declarative_base()

    class Cartao(Base):
        __tablename__ = 'cartao'

        Nome_Titular = Column(String(255))
        CPF_Titular = Column(BigInteger)
        Numero_Cartao = Column(BigInteger, primary_key=True)
        Data_Vencimento = Column(String(255))
        Tipo = Column(String(255))


    Base.metadata.create_all(engine)
    mfCartao = Cartao(Nome_Titular=nome, CPF_Titular=cpf, Numero_Cartao=numCartao, Data_Vencimento=data, Tipo=tipo)
    session.add(mfCartao)
    session.commit()
    session.close()
    success = "Cadastro concluido com sucesso!"

    return success