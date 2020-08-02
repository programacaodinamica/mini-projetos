import os
import requests


def baixar_arquivo(url, endereco):
    # faz requisição ao servidor
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print("Download finalizado. Salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()

def gerar_enderecos(sequencia, url_base, arquivo_base, dir_saida = 'output'):
    # gera a sequencia de urls e nomes de arquivo
    for i in sequencia:
        url = url_base.format(i)
        nome_arquivo = os.path.join(dir_saida, arquivo_base.format(i))
        yield (url, nome_arquivo)

if __name__ == "__main__":
    url_base = 'https://math.mit.edu/classes/18.745/Notes/Lecture_{}_Notes.pdf'
    arquivo_base = 'nota_de_aula_{}.pdf'
    for (url, nome_arquivo) in gerar_enderecos(range(1, 26), url_base, arquivo_base):
        baixar_arquivo(url, nome_arquivo)
