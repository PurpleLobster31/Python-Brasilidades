from validate_docbr import CPF, CNPJ

class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)
        if self.tipo_documento == "cpf":
            if self.valida_cpf(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF Inválido!")
        elif self.tipo_documento == "cnpj":
            if self.valida_cnpj(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ Inválido!")
        else:
            raise ValueError("Documento inválido!")
    
    def __str__(self):
        if(self.tipo_documento == "cpf"):
            return self.formata_cpf()
        elif(self.tipo_documento == "cnpj"):
            return self.formata_cnpj()
    
    def valida_cpf(self, documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida!")
        
    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
        
    def valida_cnpj(self, documento):
        if len(documento) == 14:
            validador = CNPJ()
            return validador.validate(documento)
        else:
            raise ValueError("Quantidade de dígitos inválida!")
    
    def formata_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)