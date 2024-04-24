-- create database loja;
-- use loja;
-- create table Produtos(
--     nome_produtos VARCHAR(50) NOT NULL,
--     categoria VARCHAR(50) NOT NULL,
--     marca VARCHAR(50) NOT NULL,
--     forn_prod VARCHAR(50) NOT NULL,
--     data_valid_prod DATE NOT NULL,
--     data_entrada_prod DATE NOT NULL,
--     preco_compra FLOAT NOT NULL,
--     preco_venda FLOAT NOT NULL,
--     quantidade INTEGER NOT NULL,
--     fk_estoque INT
-- );
-- select * from produto;

CREATE DATABASE Controle_de_Estoque;
USE Controle_de_Estoque;

CREATE TABLE Estoque(
    id_estoque INT AUTO_INCREMENT PRIMARY KEY,
    nome_produto VARCHAR(50) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    fornecedor VARCHAR(50),
    data_valid DATE NOT NULL,
    data_de_entrada DATE NOT NULL,
    preco_compra FLOAT NOT NULL,
    qtd_em_estoque INTEGER NOT NULL,
    fk_estoq_plo INT
);

CREATE TABLE Plo(
    id_plo INT AUTO_INCREMENT PRIMARY KEY,
    nome_prod_plo VARCHAR(50) NOT NULL,
    marca_plo VARCHAR(50) NOT NULL,
    forn_plo VARCHAR(50) NOT NULL,
    data_entrada_plo DATE NOT NULL,
    qtd_estoq_plo VARCHAR(50) NOT NULL,
    entrada_prod_plo VARCHAR(50) NOT NULL,
    saida_prod_plo VARCHAR(50) NOT NULL,
    status_disp_plo VARCHAR(50) NOT NULL,
    fk_usuario INT
);

CREATE TABLE Produtos(
    id_produtos INT AUTO_INCREMENT PRIMARY KEY,
    nome_produtos VARCHAR(50) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    forn_prod VARCHAR(50) NOT NULL,
    data_valid_prod DATE NOT NULL,
    data_entrada_prod DATE NOT NULL,
    preco_compra FLOAT NOT NULL,
    preco_venda FLOAT NOT NULL,
    quantidade INTEGER NOT NULL,
    fk_estoque INT
);


CREATE TABLE Usuario(
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    senha_hash VARCHAR(100) NOT NULL,
    email VARCHAR(50) NOT NULL,
    telefone INTEGER,
    isAdmin BOOLEAN NOT NULL
);

ALTER TABLE Estoque ADD CONSTRAINT FOREIGN KEY (fk_estoq_plo)
REFERENCES Plo(id_plo);


ALTER TABLE Plo ADD CONSTRAINT FOREIGN KEY (fk_usuario)
REFERENCES Usuario(id_usuario);


ALTER TABLE Produtos ADD CONSTRAINT FOREIGN KEY (fk_estoque)
REFERENCES Estoque(id_estoque);