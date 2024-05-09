CREATE DATABASE bd_exemplo;

CREATE TABLE tb_categoria (
	id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(60));

CREATE TABLE tb_produto (
	id_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(60),
    descricao TEXT,
    foto VARCHAR(250),
    id_categoria int,
    CONSTRAINT fk_categoria_produto 
		FOREIGN KEY (id_categoria) 
        REFERENCES tb_categoria(id_categoria)
    );

    
    

