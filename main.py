from Cpf_Cnpj import CpfCnpj

#cpf_um = Cpf("41042164886")
#print(cpf_um)
exemplo_cnpj = "35379838000112"
exemplo_cpf = "41042164886"
documento = CpfCnpj(exemplo_cnpj, "cnpj")
documento2 = CpfCnpj(exemplo_cpf, "cpf")
print(documento)
print(documento2)