import mysql.connector

class Conexao:
    
    def conectar():
        #Conectando ao banco de dados
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="usuario_exemplo",
            password="senha_exemplo",
            database="crabiz"
            )
        return mydb