from conexao import Conexao

#------------------------------------------------------------

def retorna_produto(id_produto: int) -> dict:
    mydb = Conexao.conectar()
    
    cursor = mydb.cursor(dictionary=True)
    
    sql = """
        SELECT
            p.id_produto,
            p.nome,
            p.descricao,
            format(p.preco,2,'pt_BR') as preco,
            p.foto,
            c.nome as "categoria",
            c.cor as "cor_categoria"
            FROM tb_produto p
        INNER JOIN tb_categoria c
        ON  p.id_categoria = c.id_categoria
        WHERE id_produto = %s;
        """
    valores = [id_produto]
    
    cursor.execute(sql,valores)
    
    resultado = cursor.fetchone()
    
    mydb.close()
    
    return (resultado)

#------------------------------------------------------------

def retorna_produtos(filtro:str=None) -> list:
    mydb = Conexao.conectar()
    cursor = mydb.cursor(dictionary=True)
    
    sql = """
        SELECT
            p.id_produto,
            p.nome,
            p.descricao,
            format(p.preco,2,'pt_BR') as "preco",
            p.foto,
            c.nome as "categoria",
            c.cor as "cor_categoria"
            FROM tb_produto p
        INNER JOIN tb_categoria c
        ON  p.id_categoria = c.id_categoria
        """
    if filtro != None :
        sql = sql + " WHERE c.nome = %s"
        valores = [filtro]
        cursor.execute(sql,valores)
    else:
        cursor.execute(sql)
    
    resultado = cursor.fetchall()
    
    mydb.close()
    
    return (resultado)

#--------------------------------------------------------------------

def retorna_categorias() -> list:
    mydb = Conexao.conectar()
    cursor = mydb.cursor(dictionary=True)
    
    sql = """
        SELECT
            id_categoria,
            nome,
            imagem,
            cor
            FROM tb_categoria
            ORDER BY nome
        """
    cursor.execute(sql)
    
    resultado = cursor.fetchall()

    mydb.close()
    
    return (resultado)
    