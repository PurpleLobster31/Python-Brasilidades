from Cpf_Cnpj import Documento

#cpf_um = Cpf("41042164886")
#print(cpf_um)
exemplo_cnpj = "35379838000112"
exemplo_cpf = "41042164886"
documento = Documento.cria_documento(exemplo_cnpj)
documento2 = Documento.cria_documento(exemplo_cpf)
print(documento)
print(documento2)