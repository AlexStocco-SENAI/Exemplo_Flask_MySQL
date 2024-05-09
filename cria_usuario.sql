CREATE USER 'usuario_exemplo'@'%' IDENTIFIED BY 'senha_exemplo';

GRANT ALL PRIVILEGES ON bd_exemplo.* TO 'usuario_exemplo'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;