import os
from tkinter import filedialog, messagebox


continuar = messagebox.askyesno(title='Adicionar linha', 
            message='Gostaria de selecionar um par origem e destino?')

with open(os.path.join('input', 'diretorios.csv'), 'w') as dircsv:
    # cabeçalho do CSV
    dircsv.write('origem,destino\n')
    while continuar:
        origem = filedialog.askdirectory()
        destino = filedialog.askdirectory()
        dircsv.write(f'{origem},{destino}\n')
        continuar = messagebox.askyesno(title='Adicionar linha', 
            message='Gostaria de selecionar mais um par origem e destino?')

