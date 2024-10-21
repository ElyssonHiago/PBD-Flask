from flask import Flask 
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Olá <br> Mundo!</h1>"

@app.route("/aluno")
def aluno():
    return render_template("formulario.html")

@app.route("/envio", methods=['POST'])
def envioForms():
    name = request.form["nome"]
    senha = request.form['senha']

    if senha == '123':
        mensagem = "você tá logado, bestie!"

    else:
        mensagem = "senha incorreta, tente novamente!"

    return render_template('resposta.html', m = mensagem)