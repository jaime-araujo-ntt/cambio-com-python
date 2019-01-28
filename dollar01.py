import requests
import json
import pandas as pd     # para exportar usando "pandas" como "pd" (abreviação de pandas)

def main():
    dollar = cambio_dollar()
    euro = cambio_euro()
    bitcoin = cambio_bitcoin()
    exportar_csv(dollar, euro, bitcoin)

def cambio_dollar(url = "http://data.fixer.io/api/latest?access_key=d5b76e6657d7268f23eb5048604dcfad&format=1"):    # ADD OS IMPORTS DIRECIONAIS NA FUNÇÃO PARA DEIXAR INDEPENDENTE.
    print("Estabelecendo conexão com o link... ")
    response = requests.get(url)
    if response.status_code == 200:
        print("Conseguiu se conectar...")
        dados = response.json()  # pega o json do site na variavel response
        taxa_usd = dados['rates']['USD']
        taxa_brl = dados['rates']['BRL']
        real = taxa_brl / taxa_usd
        real = round(real, 2)    # aproximação para 2 casas decimais
        return real  # o return serve para mandar o valor para onde a função foi chamada>>> MAIN
    else:
        print("site com algum problema!")

def cambio_euro(url = "http://data.fixer.io/api/latest?access_key=d5b76e6657d7268f23eb5048604dcfad&format=1"):
    print("Estabelecendo conexão com o link... ")
    response = requests.get(url)
    if response.status_code == 200:
        print("Conseguiu se conectar...")
        dados = response.json()  # pega o json do site na variavel response
        taxa_eur = dados['rates']['EUR']
        taxa_brl = dados['rates']['BRL']
        real = taxa_brl / taxa_eur
        real = round(real, 2)  # aproximação para 2 casas decimais
        return real
    else:
        print("site com algum problema!")

def cambio_bitcoin(url = "http://data.fixer.io/api/latest?access_key=d5b76e6657d7268f23eb5048604dcfad&format=1"):
    print("Estabelecendo conexão com o link... ")
    response = requests.get(url)
    if response.status_code == 200:
        print("Conseguiu se conectar...")
        dados = response.json()  # pega o json do site na variavel response
        taxa_btc = dados['rates']['BTC']
        taxa_brl = dados['rates']['BRL']
        real = taxa_brl / taxa_btc
        real = round(real, 2)  # aproximação para 2 casas decimais
        return real
    else:
        print("site com algum problema!")

def exportar_csv(dollar, euro, bitcoin):    #csv modelo padrao que o EXCEL tambem lê.
    linha = {'Dollar - USD': [dollar], 'Euro - EUR': [euro], 'Bitcoin - BTC': [bitcoin]}   # criando objeto
    frame = pd.DataFrame(linha, columns = ['Dollar - USD', 'Euro - EUR', 'Bitcoin - BTC']) # como vai para a tela do EXCEL
    frame.to_csv('moeda.csv')   # nomeando o arquivo
    print('Dados salvo na tabela!')


# pede para que o programa execute a função main
if __name__ == '__main__':
    main()
