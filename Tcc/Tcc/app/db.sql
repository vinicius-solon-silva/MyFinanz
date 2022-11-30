CREATE TABLE usuario (
    Nome varchar(255),
    Email varchar(255),
    CPF bigint not null primary key,
    Data_Nasc varchar(255),
    Senha varchar(255),
    Cargo_Profissional varchar(255),
    Salario_Mensal float
);

CREATE TABLE cartao (
    Nome_Titular varchar(255),
    Email varchar(255),
    CPF_Titular bigint not null foreign key references usuario(CPF),
    Numero_Cartao bigint,
    Data_Vencimento varchar(255),
    Tipo varchar(255)
);

CREATE TABLE categoria (
    id int primary key,
    Nome varchar(255),
    Descricao varchar(255)
);

CREATE TABLE receita (
    Descricao varchar(255),
    Quantia float,
    Categoria int foreign key references categoria(id),
    Data_Recebida varchar(255)
);

CREATE TABLE despesa (
    Descricao varchar(255),
    Categoria int foreign key references categoria(id),
    Quantia float,
    Data_Vencimento varchar(255),
    Pago bit
);

CREATE TABLE objetivo (
    Descrição varchar(255),
    Limite float
);

