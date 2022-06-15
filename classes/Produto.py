from classes.Validacoes import Validacoes
class Produto:
    def __init__(self,nome:str,valor:float,descricao:str,quantidade:int,codigo:int=0):
        self.codigo = codigo
        self.nome = nome
        self.valor = valor
        self.descricao = descricao
        self.quantidade = quantidade

        self._lista_erros = []
        self._validacoes = Validacoes()

        if self._lista_erros != []:
            erro = {
                "codigo":405,
                "data":self._lista_erros
            }
            return erro 

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo:int):
        if self.__validar_campo_vazio(codigo):
            self._codigo = codigo
        else:
            # self._lista_erros.append(self._validacoes.gerar_codigo_status(400,"Erro na validacao do codigo"))
            print("Erro na validacao do codigo")


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        if type(nome) == str and len(nome)<201 or self.__validar_campo_vazio(nome):
            self._nome = nome
        else:
            # self._lista_erros.append(self._validacoes.gerar_codigo_status(400,"Erro na validacao do nome"))
            print("Erro na validacao do nome")


    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        # if type(valor) == float and not self.__validar_campo_vazio(valor):
        if self.__validar_campo_vazio(valor):
            self._valor = valor
        else:
            # self._lista_erros.append(self._validacoes.gerar_codigo_status(400,"Erro na validacao do valor"))
            print("Erro na validacao do valor")


    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        
        if type(descricao) == str and len(descricao)<401 or self.__validar_campo_vazio(descricao):
            self._descricao = descricao
        else:
            # self._lista_erros.append(self._validacoes.gerar_codigo_status(400,"Erro na validacao da descrição"))
            print("Erro na validacao da descrição")


    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        # if type(quantidade) == int and not self.__validar_campo_vazio(quantidade):
        if self.__validar_campo_vazio(quantidade):
            self._quantidade = quantidade
        else:
            # self._lista_erros.append(self._validacoes.gerar_codigo_status(400,"Erro na validacao da quantidade"))
            print("Erro na validacao da quantidade")

    def retornar_dados_insercao(self)->list:
        dados = (self.nome,self.valor,self.descricao,self.quantidade)
        return [dados]
    
    def retornar_dados_alterar(self)->list:
        print(self.nome)
        dados = (self.nome,self.valor,self.descricao,self.quantidade,self.codigo)
        return [dados]

    def __validar_campo_vazio(self,campo)->bool:
        if campo == "" or campo == None:
            return False
        else:
            return True

    
        