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

# @app.route("/cadastrar",methods=["GET","POST"])
# # @app.route("/cadastrar",methods=["GET"])
# def cadastrar():

#     # dados_cadastro = {
#     #     'nome' : request.form.get('nome'),
#     #     'valor' : request.form.get('valor'),
#     #     'descricao' : request.form.get('descricao'),
#     #     'quantidade' : request.form.get('quantidade')
#     # }
#     # # print(request.form.get('senha'))
#     # produto = ProdutoCrud()
    
#     return render_template('cadastro.html')
#     # return render_template('cadastro.html')

@app.route("/cadastrar",methods=["POST"])
def cadastrar():
    dados_cadastro = {
        'nome' : request.form.get('nome'),
        'valor' : request.form.get('valor'),
        'descricao' : request.form.get('descricao'),
        'quantidade' : request.form.get('quantidade')
    }
    produto = ProdutoCrud()
    produto.cadastrar_produto(dados_cadastro)
    return produto.cadastrar_produto(dados_cadastro)

@app.route("/alterar",methods=["POST"])
def alterar():
    dados_alterados = {
        'codigo' : request.form.get('codigo'),
        'nome' : request.form.get('nome'),
        'valor' : request.form.get('valor'),
        'descricao' : request.form.get('descricao'),
        'quantidade' : request.form.get('quantidade')
    }
    produto = ProdutoCrud()
    return produto.alterar_produto(dados_alterados)

@app.route("/deletar",methods=["POST"])
def deletar():
    codigo_delecao = {
        'codigo' : request.form.get('codigo')
    }
    produto = ProdutoCrud()
    return produto.deletar_produto(codigo_delecao)

@app.errorhandler(404) 
def not_found(e):
    return render_template("404.html") 

@app.errorhandler(405) 
def not_found(e):
    return render_template("404.html") 

if __name__ == "__main__":
    app.run(debug=False)