from flask import Flask, render_template
from conexao import Conexao

app = Flask(__name__)

@app.route("/")
def pag_inicial():
    return render_template("index.html")



app.run(debug=True)