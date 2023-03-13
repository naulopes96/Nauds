import os

nome_pasta = './EIT_100323'

arq_pasta = []


for diretorio, subpastas, arquivos in os.walk(nome_pasta):
    for arquivo in arquivos:
        arq_pasta.append(os.path.join(diretorio,arquivo))

print (arq_pasta)