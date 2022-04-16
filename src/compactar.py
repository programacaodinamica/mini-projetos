import os
from tkinter import filedialog
from zipfile import ZipFile, ZIP_DEFLATED


def compactar_tudo(diretorio, ignore_zips=True):
    nomesarquivos = os.listdir(diretorio)
    if ignore_zips:
        nomesarquivos = [fn for fn in nomesarquivos if not fn.endswith('.zip')]

    for nome in nomesarquivos:
        fullpath = os.path.join(diretorio, nome)
        if os.path.isdir(fullpath):
            nomezip = os.path.join(diretorio, nome + '.zip')
            arquivozip = ZipFile(nomezip, "a", compression=ZIP_DEFLATED)
            for raiz, dirs, arquivos in os.walk(fullpath):
                for arq in arquivos:
                    relativo = os.path.relpath(raiz, diretorio)
                    arquivozip.write(os.path.join(raiz, arq),
                                     os.path.join(relativo, arq))
            arquivozip.close()
        else:
            semextensao = nome.split('.')[0]
            nomezip = os.path.join(diretorio, semextensao + '.zip')
            arquivozip = ZipFile(nomezip, "w", compression=ZIP_DEFLATED)
            arquivozip.write(fullpath, nome)
            arquivozip.close()

    return len(nomesarquivos)

if __name__ == '__main__':
    # pasta = input("Digite o endereço da pasta a ser compactada: ")
    pasta = filedialog.askdirectory()
    print(f"Compactando arquivos em {pasta}")
    n = compactar_tudo(pasta)
    print(f"{n} arquivos compactados com sucesso")