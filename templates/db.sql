-- comandos para inserir dentro do banco de dados.


CREATE DATABASE controle_de_estoque;
USE controle_de_estoque;

CREATE TABLE estoque(
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
CREATE TABLE plo(
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
CREATE TABLE produtos(
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
CREATE TABLE usuario(
id_usuario INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(50) NOT NULL,
senha_hash VARCHAR(100) NOT NULL,
email VARCHAR(50) NOT NULL,
telefone INTEGER,
isAdmin BOOLEAN NOT NULL
);
ALTER TABLE estoque ADD CONSTRAINT FOREIGN KEY (fk_estoq_plo)
REFERENCES plo(id_plo); 

ALTER TABLE plo ADD CONSTRAINT FOREIGN KEY (fk_usuario)
REFERENCES usuario(id_usuario);

ALTER TABLE produtos ADD CONSTRAINT FOREIGN KEY (fk_estoque)
REFERENCES estoque(id_estoque);
INSERT INTO produtos(nome_produtos, marca, forn_prod, data_valid_prod, data_entrada_prod, preco_compra, preco_venda,quantidade)
VALUES
('Refrigerante','Coca-Cola','Ambev',20241106,20240418,324.76,7.00,12),
('Cerveja','Stella','Ambev',20241227,20240418,420.50,10.00,4),
('Vinhos','Catena Zapata','Fox importadora',20261124,20240418,15.000,1.980,10),
('Agua','Agua na caixa','Agua na caixa',20250113,20240418,1.267,12.00,12);
INSERT INTO estoque(nome_produto, marca, fornecedor, data_valid, data_de_entrada, preco_compra, qtd_em_estoque)
VALUES
('Refrigerante', 'Coca-Cola','Ambev',20250415,20240418,324.76,210),
('Cerveja','Stella','Ambev',20250201,20240418,420.50,210),
('Vinhos','Catena Zapata','Fox importadora',20240720,20240418,15.000,10),
('Agua','Agua na caixa','Agua na caixa',20240604,20240418,1.267,12);
INSERT INTO plo(nome_prod_plo, marca_plo, forn_plo, data_entrada_plo, qtd_estoq_plo, entrada_prod_plo, saida_prod_plo, status_disp_plo)
VALUES
('Refrigerante', 'Coca-Cola','Ambev',20240418,210,'Coca-Cola','Coca-Cola','Ativo'),
('Cerveja','Stella','Ambev',20240418,210,'Stella','Stella','Ativo'),
('Vinhos','Catena Zapata','Fox importadora',20240418,10,'Catena Zapata','Catena Zapata','Ativo'),
('Agua','Agua na caixa','Agua na caixa',20240418,12,'Agua na caixa','Agua na caixa','Ativo');
INSERT INTO usuario(nome, senha_hash, email, telefone, isAdmin)
VALUES
('Shaihanne','Shaihanne','shaihanne@fecaf.com.br',1196285-1861,1),
('Lucas','Lucas','lucas@fecaf.com.br',1198842-6622,1),
('Pedro','Pedro','pedro@fecaf.com.br',1194430-1190,0),
('Geovane','Geovane','geovane@fecaf.com.br',1194411-9962,0);
select * from usuario;