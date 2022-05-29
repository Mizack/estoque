from flask import Flask,render_template,request
from crud.ProdutoCrud import ProdutoCrud

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/listar")
def listar():
    produto = ProdutoCrud()
    return produto.listar_produtos()

@app.route("/cadastrar",methods=["POST"])
def cadastrar():
    dados_cadastro = {
        'nome' : request.form.get('nome'),
        'valor' : request.form.get('valor'),
        'descricao' : request.form.get('descricao'),
        'quantidade' : request.form.get('quantidade')
    }
    produto = ProdutoCrud()
    return produto.cadastrar_produto(dados_cadastro)

@app.errorhandler(404) 
def not_found(e):
    return render_template("404.html") 

@app.errorhandler(405) 
def not_found(e):
    return render_template("404.html") 

if __name__ == "__main__":
    app.run(debug=False)