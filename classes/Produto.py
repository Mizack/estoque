from classes.Validacoes import Validacoes
class Produto:

    def __init__(self,nome:str,valor:float,descricao:str,quantidade:int,codigo:int=0):
        self.codigo = codigo
        self.nome = nome
        self.valor = valor
        self.descricao = descricao
        self.quantidade = quantidade

        self.__lista_erros = []
        self.__validacoes = Validacoes()

        if self.__lista_erros != []:
            erro = {
                "codigo":405,
                "data":self.__lista_erros
            }
            return erro 

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo:int):
        if not self.__validar_campo_vazio(codigo):
            self.__codigo = codigo
        else:
            self.__lista_erros.append(self.__validacoes.gerar_codigo_status(400,"Erro na validacao do codigo"))


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if type(nome) == str and len(nome)<201 or not self.__validar_campo_vazio(nome):
            self.__nome = nome
        else:
            
            self.__lista_erros.append(self.__validacoes.gerar_codigo_status(400,"Erro na validacao do nome"))


    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        # if type(valor) == float and not self.__validar_campo_vazio(valor):
        if not self.__validar_campo_vazio(valor):
            self.__valor = valor
        else:
            self.__lista_erros.append(self.__validacoes.gerar_codigo_status(400,"Erro na validacao do valor"))


    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        if type(descricao) == str and len(descricao)<401 or not self.__validar_campo_vazio(descricao):
            self.__descricao = descricao
        else:
            self.__lista_erros.append(self.__validacoes.gerar_codigo_status(400,"Erro na validacao da descrição"))


    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        # if type(quantidade) == int and not self.__validar_campo_vazio(quantidade):
        if not self.__validar_campo_vazio(quantidade):
            self.__quantidade = quantidade
        else:
            self.__lista_erros.append(self.__validacoes.gerar_codigo_status(400,"Erro na validacao da quantidade"))

    def retornar_dados_insercao(self)->list:
        dados = (self.nome,self.valor,self.descricao,self.quantidade)
        return [dados]
    
    def retornar_dados_alterar(self)->list:
        dados = (self.nome,self.valor,self.descricao,self.quantidade,self.codigo)
        return [dados]

    def __validar_campo_vazio(self,campo)->bool:
        if campo == "" or campo == None:
            return False
        else:
            return True

    
        