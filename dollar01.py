import requests
import json

def main():
    cambio_euro()
    cambio_dollar()

def cambio_dollar(): #ADD OS IMPORTS DIRECIONAIS NA FUNÇÃO PARA DEIXAR INDEPENDENTE.
    print("Estabelecendo conexão com o link... ")
    response = requests.get("http://data.fixer.io/api/latest?access_key=d5b76e6657d7268f23eb5048604dcfad&format=1")
    if response.status_code == 200:
        print("Conseguiu se conectar...")
        dados = response.json()  # pega o json do site na variavel response
        taxa_usd = dados['rates']['USD']
        taxa_brl = dados['rates']['BRL']
        real = taxa_brl / taxa_usd
        print("1 Dollar equivale a %.2f Reais" % real)

def cambio_euro():
    print("Estabelecendo conexão com o link... ")
    response = requests.get("http://data.fixer.io/api/latest?access_key=d5b76e6657d7268f23eb5048604dcfad&format=1")
    if response.status_code == 200:
        print("Conseguiu se conectar...")
        dados = response.json()  # pega o json do site na variavel response
        taxa_eur = dados['rates']['EUR']
        taxa_brl = dados['rates']['BRL']
        real = taxa_brl / taxa_eur
        print("1 Euros equivale a %.2f Reais" % real)

if __name__ == '__main__':
    main()