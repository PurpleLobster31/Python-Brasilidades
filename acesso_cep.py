class BuscaEndereco:
    def __init__(self, cep):
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")
    
    def __str__(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"
    
    def valida_cep(self, cep):
        return len(cep) == 8
        