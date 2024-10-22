#4 - Altere outro desses testes de unidade para que leia uma massa de teste a partir de um arquivo csv
import csv

def ler_csv(arquivo_csv):
    dados_csv = []
    try:
        with open(arquivo_csv, newline='') as massa:
         tabela = csv.reader(massa, delimiter=',')
        next(tabela)
        for linha in tabela:
                dados_csv.append(linha)
                return dados_csv
    except FileNotFoundError:
                print(f'Arquivo não encontrado: {arquivo_csv}')
    except Exception as fail:
                print(f'Falha imprevista: {fail}')
                
            