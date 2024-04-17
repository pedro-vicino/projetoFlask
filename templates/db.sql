create database loja;
use loja;
create table produto(
    id_produto int primary key auto_increment not null,
    nome_produto varchar(60) not null,
    quantidade_produto int not null
);
select * from produto;