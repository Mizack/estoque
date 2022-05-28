import sys
sys.path.append(".")
from classes.Banco import Banco
from classes.Produto import Produto
from classes.Validacoes import Validacoes
import json

class ProdutoCrud:
    def __init__(self) -> None:
        self.banco = Banco()
        self.validacoes = Validacoes()

    def listar_produtos(self):
        try:
            sql = 'SELECT * FROM TB_PRODUTO'
            self.banco.cursor.execute(sql)
            resultado = self.banco.cursor.fetchall()
            return self.__listagem(resultado)
        except:
            print('Erro de inserção')
            return False

    def __listagem(self,resultado):
        json_retornado = []
        for dados_retornados in resultado:
            sub_json = {
                'codigo':dados_retornados[0],
                'nome':dados_retornados[1],
                'valor':dados_retornados[2],
                'descricao':dados_retornados[3],
                'quantidade':dados_retornados[4],
                'ultima_alteracao':dados_retornados[5]
            }
            json_retornado.append(sub_json)
        return json_retornado

    def cadastrar_produto(self,dados):
        gabarito = ['nome','valor','descricao','quantidade']

        # for chave_esperada in gabarito:
            # if not self.validacoes.validar_chave_dict(dados,chave_esperada):
            #     print('erro de validacao')
            #     return False # colocar um json como retorno
        
        produto = Produto(
            nome=dados['nome'],
            valor=dados['valor'],
            descricao=dados['descricao'],
            quantidade=dados['quantidade']
        ).retornar_dados_insercao()

        try:
            sql = "INSERT INTO TB_PRODUTO(NM_PRODUTO,VL_PRODUTO,DS_DESCRICAO,QT_PRODUTO)VALUES(?,?,?,?)"
            self.banco.cursor.executemany(sql,produto)
            self.banco.conexao.commit()
        except:
            print('erro')
            return False # colocar um json como retorno