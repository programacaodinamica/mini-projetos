import os
import shutil
from csv import DictReader
from pathlib import PurePath


def copiar_origem_destino(nomearquivo):
    with open(nomearquivo) as meucsv:
        reader = DictReader(meucsv)
        for linha in reader:
            orig = linha['origem']
            dest = linha['destino']
            if os.path.exists(dest):
                nome = PurePath(orig).name
                dest = os.path.join(dest, nome)
            # faz a cópia da pasta e tudo em seu interior
            shutil.copytree(orig, dest)
            print(dest, 'foi copiado com sucesso!')

if __name__ == "__main__":
    copiar_origem_destino('input/diretorios.csv')

