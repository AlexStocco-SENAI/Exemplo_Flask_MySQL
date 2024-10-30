from flask import Flask, render_template, request, jsonify
from conexao import Conexao
from produtos import *

app = Flask(__name__)

#PÁGINA INICIAL
@app.route("/")
def pag_inicial():
    return render_template("index.html")

#---------------------------------------------------


#PRODUTOS VIA URL
@app.route("/produtos_via_url", methods=["GET"])
def pag_produtos_via_url():
    
    filtro = request.args.get('filtro')
    
    lista_produtos = retorna_produtos(filtro)
    
    lista_categorias = retorna_categorias()
    
    return render_template("produtos_via_url.html", 
                           lista_produtos = lista_produtos,
                           lista_categorias = lista_categorias)


@app.route("/sobre_produto_url/<id_produto>")
def pag_sobre_produto(id_produto):
    id_produto = id_produto
    produto = retorna_produto(id_produto)
    return render_template("sobre_produto_url.html", produto=produto)

@app.route("/sobre_produto_url")
def pag_sobre_produto2():
    id_produto  = int(request.args.get('produto'))
    produto = retorna_produto(id_produto)
    return render_template("sobre_produto_url.html", produto=produto)
    
#-----------------------------------------------------------------

#PRODUTOS VIA API
@app.route("/produtos_via_ajax", methods=["GET"])
def pag_produtos_via_ajax():
    return render_template("produtos_via_ajax.html" )

@app.route("/api/get_categorias")
def api_get_categorias():
    lista_categorias = retorna_categorias()
    return jsonify(lista_categorias), 200

@app.route("/api/get_produtos", methods=['GET'])
def api_get_produtos():
    lista_produtos = retorna_produtos()
    return jsonify(lista_produtos), 200

@app.route("/api/get_produtos/<filtro>", methods=['GET'])
def api_get_produtos_filtro(filtro):
    lista_produtos = retorna_produtos(filtro)
    return jsonify(lista_produtos), 200
    
@app.route("/api/sobre_produto_ajax/<produto>")
def pag_get_sobre_produto(produto):
    sobre_produto = retorna_produto(produto)
    return jsonify(sobre_produto)


#-----------------------------------------------------------------
#app.run(debug=True)
app.run(host="0.0.0.0", port=8000)
