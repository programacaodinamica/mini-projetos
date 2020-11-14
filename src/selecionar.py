import os
from tkinter import filedialog, messagebox
from copiar import copiar_origem_destino


def deve_continuar():
    return messagebox.askyesno(title='Adicionar linha', 
            message='Gostaria de selecionar um par origem e destino?')

def construir_origem_destino(nomearquivo, modo='w'):
    with open(nomearquivo, modo) as dircsv:
        if modo == 'w':
            # cabeçalho do CSV
            dircsv.write('origem,destino\n')
        while deve_continuar():
            origem = filedialog.askdirectory()
            destino = filedialog.askdirectory()
            dircsv.write(f'{origem},{destino}\n')

if __name__ == "__main__":
    arquivo = os.path.join('input', 'diretorios.csv')
    if os.path.exists(arquivo):
        construir_origem_destino(arquivo, 'a')
    else:
        construir_origem_destino(arquivo)
    copiar_origem_destino(arquivo)

