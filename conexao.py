import mysql.connector

class Conexao:
    
    # def conectar():
    #     #Conectando ao banco de dados
    #     mydb = mysql.connector.connect(
    #         host="127.0.0.1",
    #         user="usuario_exemplo",
    #         password="senha_exemplo",
    #         database="bd_exemplo"
    #         )
    #     return mydb

    def conectar():
        #Conectando ao banco de dados
        mydb = mysql.connector.connect(
            host="banco-de-dados-godofredo.mysql.database.azure.com",
            user="godoadmin",
            password="Alexlindao@123",
            database="bd_exemplo"
            )
        return mydb