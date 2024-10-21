from flask import Flask 

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Olá <br> Mundo!</h1>"

@app.route("/aluno/<nome>")
def aluno(nome):
    return nome