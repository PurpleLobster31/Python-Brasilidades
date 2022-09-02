import requests
from acesso_cep import BuscaEndereco

cep = "05625040"
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

# r = requests.get("https://viacep.com.br/ws/01001000/json/")
# print(r.text)

a = objeto_cep.acessa_cep()
print(a.text)