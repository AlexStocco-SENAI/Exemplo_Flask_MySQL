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
    
    
#-----------------------------------------------------------------

#PRODUTOS VIA API
@app.route("/produtos_via_ajax", methods=["GET"])
def pag_produtos_via_ajax():
    return render_template("produtos_via_ajax.html" )

@app.route("/api/get_categorias")

@app.route("/api/get_produtos", methods=['GET'])
def api_get_produtos():
    lista_produtos = retorna_produtos()
    return jsonify(lista_produtos), 200

@app.route("/api/get_produtos/<filtro>", methods=['GET'])
def api_get_produtos_filtro(filtro):
    lista_produtos = retorna_produtos(filtro)
    return jsonify(lista_produtos), 200
    


#-----------------------------------------------------------------
app.run(debug=True)
#app.run(host="0.0.0.0", port=8080)