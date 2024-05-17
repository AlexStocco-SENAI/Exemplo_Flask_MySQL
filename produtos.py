from conexao import Conexao

#------------------------------------------------------------

def retorna_produto(id_produto: int) -> dict:
    mydb = Conexao.conectar()
    
    cursor = mydb.cursor()
    
    sql = """
        SELECT
            p.id_produto,
            p.nome,
            p.descricao,
            p.preco,
            p.foto,
            c.nome as "categoria",
            c.cor as "cor_categoria"
            FROM tb_produto p
        INNER JOIN tb_categoria c
        ON  p.id_categoria = c.id_categoria
        WHERE id_produto = %d;
        """
    valores = (id_produto,)
    
    cursor.execute(sql,valores)
    
    resultado = cursor.fetchone()
    
    mydb.close()
    
    dicionario_produto ={
        "id_produto":resultado[0],
        "nome":resultado[1],
        "descricao":resultado[2],
        "preco":resultado[3],
        "foto":resultado[4],
        "categoria":resultado[5],
        "cor_categoria":resultado[6]
    }
    
    return (dicionario_produto)

#------------------------------------------------------------

def retorna_produtos(filtro:str=None) -> list:
    mydb = Conexao.conectar()
    cursor = mydb.cursor()
    
    sql = """
        SELECT
            p.id_produto,
            p.nome,
            p.descricao,
            format(p.preco,2,'pt_BR'),
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
    
    lista_produtos = []
    
    for produto in resultado:
        lista_produtos.append({
            "id_produto":produto[0],
            "nome":produto[1],
            "descricao":produto[2],
            "preco":produto[3],
            "foto":produto[4],
            "categoria":produto[5],
            "cor_categoria":produto[6]
        })
    
    return (lista_produtos)

#--------------------------------------------------------------------

def retorna_categorias() -> list:
    mydb = Conexao.conectar()
    cursor = mydb.cursor()
    
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
    
    lista_categorias = []
    
    for categoria in resultado:
        lista_categorias.append({
            "id_categoria":categoria[0],
            "nome":categoria[1],
            "imagem":categoria[2],
            "cor":categoria[3]
        })
    
    return (lista_categorias)
    