class Validacoes:
    
    def gerar_codigo_status(self,codigo:int,mensagem:str)->dict:
        codigo_status = {
            "codigo":codigo,
            "data":mensagem
        }
        return codigo_status