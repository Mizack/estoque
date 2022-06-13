from flask import Flask,render_template,request
from crud.ProdutoCrud import ProdutoCrud

app = Flask(__name__)

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

@app.route("/deletar",methods=['POST'])
def deletar():
    codigo_delecao = {
        'codigo' : request.form.get('codigo')
    }
    produto = ProdutoCrud()
    return produto.deletar_produto(codigo_delecao)

@app.errorhandler(404) 
def not_found(e):
    erro = {
            "codigo":404,
            "data":"Erro de requisição."
        }
    return erro 

@app.errorhandler(405) 
def not_found(e):
    erro = {
            "codigo":405,
            "data":"Parâmetros inválidos."
        }
    return erro 

@app.errorhandler(500) 
def not_found(e):
    erro = {
            "codigo":500,
            "data":"Não foi possível processar a requisição."
        }
    return erro 

if __name__ == "__main__":
    app.run(debug=False)