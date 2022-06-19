import sys
sys.path.append(".")
from classes.Banco import Banco
from classes.Produto import Produto
from classes.Validacoes import Validacoes
import json

class ProdutoCrud:
    def __init__(self) -> None:
        self.__banco = Banco()
        self.__validacoes = Validacoes()

    def listar_produtos(self)->dict:
        try:
            sql = 'SELECT * FROM TB_PRODUTO'
            self.__banco.cursor.execute(sql)
            resultado = self.__banco.cursor.fetchall()
            
            return self.__listagem(resultado)
        except:
            return self.__validacoes.gerar_codigo_status(500,"erro ao listar")

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

    def cadastrar_produto(self,dados:dict)->dict:
        gabarito = ['nome','valor','descricao','quantidade']
        for chave in gabarito:
            if chave not in dados:
                return self.__validacoes.gerar_codigo_status(405,f"Parâmetro '{chave}' inválido.")

        produto = Produto(
            nome=dados['nome'],
            valor=float(dados['valor']),
            descricao=dados['descricao'],
            quantidade=int(dados['quantidade'])
        )
        if produto.erro_instancia() == True:
            dado_inserido = produto.retornar_dados_insercao()

            try:
                sql = "INSERT INTO TB_PRODUTO(NM_PRODUTO,VL_PRODUTO,DS_DESCRICAO,QT_PRODUTO)VALUES(%s,%s,%s,%s)"
                self.__banco.cursor.executemany(sql,dado_inserido)
                self.__banco.conexao.commit()
                return self.__validacoes.gerar_codigo_status(200,"cadastrado com sucesso")
            except:
                return self.__validacoes.gerar_codigo_status(500,"erro ao cadastrar")
        else:
            return produto.erro_instancia()

    def alterar_produto(self,dados)->dict:
        gabarito = ['nome','valor','descricao','quantidade','codigo']
        for chave in gabarito:
            if chave not in dados:
                return self.__validacoes.gerar_codigo_status(405,f"Parâmetro '{chave}' inválido.")

        validar_existencia_dados = self.__verificar_exis_item(dados['codigo'])
        
        if validar_existencia_dados == False:
            return self.__validacoes.gerar_codigo_status(202,"Não existe nenhuma correspondência para o valor informado.")
        elif type(validar_existencia_dados) == dict:
            return validar_existencia_dados

        produto = Produto(
            nome=dados['nome'],
            valor=dados['valor'],
            descricao=dados['descricao'],
            quantidade=dados['quantidade'],
            codigo=dados['codigo']
        )
        if produto.erro_instancia() == True:
            lista_alterado = produto.retornar_dados_alterar()
            try:
                sql = """UPDATE TB_PRODUTO SET NM_PRODUTO = %s,
                    VL_PRODUTO = %s,
                    DS_DESCRICAO = %s,
                    QT_PRODUTO = %s
                    WHERE ID_PRODUTO = %s;"""

                self.__banco.cursor.executemany(sql,lista_alterado)
                self.__banco.conexao.commit()
                return self.__validacoes.gerar_codigo_status(200,"alterado com sucesso")
            except:
                return self.__validacoes.gerar_codigo_status(500,"erro ao alterar")
        else:
            return produto.erro_instancia()

    def deletar_produto(self,dados)->dict:
        validar_existencia_dados = self.__verificar_exis_item(dados['codigo'])
        
        if validar_existencia_dados == False:
            return self.__validacoes.gerar_codigo_status(202,"Não existe nenhuma correspondência para o valor informado.")
        elif type(validar_existencia_dados) == dict:
            return validar_existencia_dados
        try:
            sql = "DELETE FROM TB_PRODUTO WHERE ID_PRODUTO = %s"
            self.__banco.cursor.execute(sql,([dados['codigo']]))
            self.__banco.conexao.commit()
            return self.__validacoes.gerar_codigo_status(200,"excluido com sucesso")
        except:
            return self.__validacoes.gerar_codigo_status(500,"erro ao excluir")

    def __verificar_exis_item(self,codigo):
        try:
            codigo = int(codigo)
        except:
            return self.__validacoes.gerar_codigo_status(405,f"Parâmetro inválido.")
        try:
            sql = 'SELECT * FROM TB_PRODUTO where ID_PRODUTO = %s'
            self.__banco.cursor.execute(sql,int(codigo))
            resultado = self.__banco.cursor.fetchall()
            if resultado == () or not resultado:
                return False
            else:
                return True
        except:
            raise self.__validacoes.gerar_codigo_status(500,"Erro ao listar")