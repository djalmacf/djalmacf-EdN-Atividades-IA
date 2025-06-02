import csv

def escrever_csv(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['Nome', 'Idade', 'Cidade'])
            for linha in dados:
                escritor.writerow(linha)
        print(f"Dados salvos em {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

dados = [
    ['Gabriela', 30, 'Brasília'],
    ['Lucas', 27, 'Rio de Janeiro'],
    ['José', 35, 'São Paulo']
]

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo CSV: ").strip()
    escrever_csv(nome_arquivo, dados)
