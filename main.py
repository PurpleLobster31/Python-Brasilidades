import requests
from acesso_cep import BuscaEndereco

cep = "13416216"
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)


#bairro, cidade, uf = objeto_cep.acessa_cep()

#print(bairro, cidade, uf)