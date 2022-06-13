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

    def listar_produtos(self)->dict:
        try:
            sql = 'SELECT * FROM TB_PRODUTO'
            self.banco.cursor.execute(sql)
            resultado = self.banco.cursor.fetchall()
            
            return self.__listagem(resultado)
        except:
            return self.validacoes.gerar_codigo_status(500,"erro ao listar")

    def __listagem(self,resultado)->dict:
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
        json_final = {
            "codigo":200,
            "mensagem":json_retornado
        }
        return json_final

    def cadastrar_produto(self,dados)->dict:
        gabarito = ['nome','valor','descricao','quantidade']
        # print(dados)
        produto = Produto(
            nome=dados['nome'],
            valor=float(dados['valor']),
            descricao=dados['descricao'],
            quantidade=int(dados['quantidade'])
        )
        dado_inserido = produto.retornar_dados_insercao()

        try:
            sql = "INSERT INTO TB_PRODUTO(NM_PRODUTO,VL_PRODUTO,DS_DESCRICAO,QT_PRODUTO)VALUES(?,?,?,?)"
            self.banco.cursor.executemany(sql,dado_inserido)
            self.banco.conexao.commit()
            return self.validacoes.gerar_codigo_status(200,"cadastrado com sucesso")
        except:
            return self.validacoes.gerar_codigo_status(500,"erro ao cadastrar")

    def alterar_produto(self,dados)->dict:
        gabarito = ['nome','valor','descricao','quantidade']
        
        produto = Produto(
            nome=dados['nome'],
            valor=dados['valor'],
            descricao=dados['descricao'],
            quantidade=dados['quantidade'],
            codigo=dados['codigo']
        )
        lista_alterado = produto.retornar_dados_alterar()
        try:
            sql = """UPDATE TB_PRODUTO SET NM_PRODUTO = ?,
                VL_PRODUTO = ?,
                DS_DESCRICAO = ?,
                QT_PRODUTO = ?
                WHERE ID_PRODUTO = ?;"""

            self.banco.cursor.executemany(sql,lista_alterado)
            self.banco.conexao.commit()
            return self.validacoes.gerar_codigo_status(200,"alterado com sucesso")
        except:
            return self.validacoes.gerar_codigo_status(500,"erro ao alterar")

    def deletar_produto(self,dados)->dict:
        try:
            sql = "DELETE FROM TB_PRODUTO WHERE ID_PRODUTO = ?"
            self.banco.cursor.execute(sql,([dados['codigo']]))
            self.banco.conexao.commit()
            return self.validacoes.gerar_codigo_status(200,"excluido com sucesso")
        except:
            return self.validacoes.gerar_codigo_status(500,"erro ao excluir")

