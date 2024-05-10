from flask import Flask, render_template
from conexao import Conexao
from produtos import *

app = Flask(__name__)

@app.route("/")
def pag_inicial():
    return render_template("index.html")

@app.route("/produtos_via_url", methods=["GET"])
def pag_produtos_via_url():
    lista_produtos = retorna_produtos()
    return render_template("produtos_via_url.html", lista_produtos = lista_produtos)

@app.route("/produtos_via_ajax", methods=["GET"])
def pag_produtos_via_ajax():
    return render_template("produtos_via_ajax.html" )

app.run(debug=True)
#app.run(host="0.0.0.0", port=8080)