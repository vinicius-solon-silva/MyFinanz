from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, BigInteger, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from AUTH import CONN_STR


def cadastrar_usuario(nome,email,cpf,data_nasc,senha,cargo_profissional,salario_mensal):

    cpf = int(cpf)
    salario_mensal = float(salario_mensal)

    engine = create_engine(CONN_STR, echo=False)
    Sessions = sessionmaker(bind=engine)
    session = Sessions()
    Base = declarative_base()


    class Usuario(Base):
        __tablename__ = 'usuario'
        children = relationship("Cartao")

        Nome = Column(String(255))
        Email = Column(String(255))
        CPF = Column(BigInteger, primary_key=True)
        Data_Nasc = Column(String(255))
        Senha = Column(String(255))
        Cargo_Profissional = Column(String(255))
        Salario_Mensal = Column(float)

        
    Base.metadata.create_all(engine)
    mfUser = Usuario(Nome=nome, CPF=cpf, Data_Nasc=data_nasc, Email=email, Senha=senha, Cargo_Profissional=cargo_profissional, Salario_Mensal=salario_mensal)
    session.add(mfUser)
    session.commit()
    session.close()
    success = "Cadastro concluido com sucesso!"

    return success


def cadastrar_cartao(nome, cpf, numCartao, data, tipo):

    cpf = int(cpf)

    engine = create_engine(CONN_STR, echo=False)
    Sessions = sessionmaker(bind=engine)
    session = Sessions()
    Base = declarative_base()

    class Cartao(Base):
        __tablename__ = 'cartao'

        Nome_Titular = Column(String(255))
        CPF_Titular = Column(BigInteger, ForeignKey("usuario.CPF"))
        Numero_Cartao = Column(BigInteger)
        Data_Vencimento = Column(String(255))
        Tipo = Column(String(255))


    Base.metadata.create_all(engine)
    mfCartao = Cartao(Nome_Titular=nome, CPF_Titular=cpf, Numero_Cartao=numCartao, Data_Vencimento=data, Tipo=tipo)
    session.add(mfCartao)
    session.commit()
    session.close()
    success = "Cadastro concluido com sucesso!"