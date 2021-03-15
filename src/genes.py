import os
from Bio import SeqIO

# Requisios = Biopython
#!pip install biopython

# Input
# ---aaattcc---cccc--
# aactgtgactgcatgcatgactgactg
# Output
# aaattcc---cccc
# tgtgactgcatgcatgactgac
def contar_no_comeco(sequencia):
    '''Conta os - no começo da sequência'''

    tracos = 0
    for c in sequencia:
        if c == '-':
            tracos = tracos + 1
        else:
            break
    return tracos

def contar_no_final(sequencia):
    '''Conta os - no final da sequência '''

    return contar_no_comeco(reversed(sequencia))

def editar_sequencias(seq):
    _inicio = contar_no_comeco(seq)
    _final = contar_no_final(seq)
    # se o final for 0, precisamos ajustar
    
    # Sim, podemos retornar duas coisas em Python
    return seq[_inicio:-_final if _final != 0 else len(seq)

if __name__ == "__main__":

  # Abrindo o arquivo fasta e lendo seu conteúdo com o módulo SeqIO
  # O SeqIO é um módulo do biopython que facilita o trabalho com arquivos de texto utilizados na bioinformática, como fasta, fastq, genbank, etc.
  # O SeqIO.parse nos permite identificar diversas features destes arquivos, por exemplo: identificador da sequência = record.id, sequência = record.seq
  with open("/content/teste/input.fasta", "r") as handle, open("output.fasta", "w") as output_handle:
    for record in SeqIO.parse(handle, "fasta"):

      # Encontrando cada sequência do arquivo e editando-as com a função "editar_sequencias"
      record.seq = editar_sequencias(record.seq)

      # Escrevendo cada uma das sequências editadas em um output no formato fasta
      SeqIO.write(record, output_handle, "fasta")
