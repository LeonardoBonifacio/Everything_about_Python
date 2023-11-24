import PyPDF2 as pyf # trabalhar com pdfs
from pathlib import Path # interagir com arquivos do nosso computador
import tabula # mexer com tabelas utilizando o pandas por tras
from pikepdf import Pdf, PdfImage
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import FreeText
import os

'''
pyf.PdfReader # Ler aquivos pdfs
pyf.PdfWriter # Escrever em arquivos pdf
pyf.PdfMerger # Juntar dois ou mais arquivos pdf
'''



'''
# Separar as paginas de um arquivo pdf

nome_arquivo = "MGLU_ER_3T20_POR.pdf"
arquivo_pdf = pyf.PdfReader(nome_arquivo) # lendo o arquivo pdf e armazenando ele em arquivo_pdf

# Um for que percorre cada pagina no arquivo pdf(por causa do .pages)
for i,pagina in enumerate(arquivo_pdf.pages, start=1):

    # pra cada pagina eu crio um arquivo pdf zerado
    arquivo_novo = pyf.PdfWriter() 

    # adciona a pagina atual nesse novo arquivo pdf vazio
    arquivo_novo.add_page(pagina) 

    # salvar o arquivo
    with Path(f'C:/Users/LUCIANO/Desktop/---Python---Margeylson/zzz_projetos/projeto_margeylson/paginas_pdf/Arquivo{i}.pdf').open(mode='wb') as arquivo_final:
        arquivo_novo.write(arquivo_final)
    # with acima cria um arquivo pdf(em modo de escrita) no caminho fornecido e escreve o que estava no arquivo novo nele
'''




# adcionando caixas de texto em um arquivo pdf

from pypdf import PdfReader, PdfWriter
from pypdf.annotations import FreeText

# Fill the writer with the pages you want
pdf = PdfWriter()
with open("C:/Users/LUCIANO/Desktop/---Python---Margeylson/zzz_projetos/projeto_margeylson/pdf.pdf", "wb") as fp:
    pdf.write(fp)
pdf_nome = "pdf"
reader = PdfReader(pdf_nome)
page = reader.pages[0]
writer = PdfWriter()
writer.add_page(page)

# Create the annotation and add it
annotation = FreeText(
    text="Hello World\nThis is the second line!",
    rect=(50, 550, 200, 650),
    font="Arial",
    bold=True,
    italic=True,
    font_size="20pt",
    font_color="00ff00",
    border_color="0000ff",
    background_color="cdcdcd",
)
writer.add_annotation(page_number=0, annotation=annotation)

# Write the annotated file to disk
with open("annotated-pdf.pdf", "wb") as fp:
    writer.write(fp)




'''
# Juntar varios pdfs em 1

paginas = [1, 14, 16] # lista das paginas que quero pegar

# criar um novo pdf
novo_pdf = pyf.PdfWriter()
for num_pagina in paginas: # percorendo cada numero das paginas que quero pegar

    # percorrendo cada arquivo pdf com a variavel de indice i + 1 dps do nome do arquivo
    nome_arquivo = f"C:/Users/LUCIANO/Desktop/---Python---Margeylson/zzz_projetos/projeto_margeylson/paginas_pdf/Arquivo{num_pagina}.pdf"

    # lendo o arquivo pdf percorrido no momento e armazenando ele na variavel arquivo pdf
    arquivo_pdf = pyf.PdfReader(nome_arquivo)

    # pegando a pagina desse arquivo pdf lido e armazenando na variavel página
    pagina = arquivo_pdf.pages[0]# o pages da uma lista com as paginas do arquivo pdf, e por isso estamos pegando pelo indice da lista

    # pegando a pagina atual da iteração e adcionando ela na variavel novo_pdf
    novo_pdf.add_page(pagina)

# salvar o nosso pdf
with Path("C:/Users/LUCIANO/Desktop/---Python---Margeylson/zzz_projetos/projeto_margeylson/paginas_pdf/Paginas_Escolhidas.pdf").open(mode='wb') as arquivo_final:
    novo_pdf.write(arquivo_final)
'''



'''
# Mesclar dois ou mais pdfs em 1

# Cria uma lista para mesclar os arquivos
pdf_mesclado = pyf.PdfMerger()

# Passa o nome dos arquivos e seu local para as variáveis
arquivo1 = "MGLU_ER_3T20_POR.pdf"
arquivo2 = "MGLU_ER_4T20_POR.pdf"

# Adciona os arquivos na "lista" do PdfMerger
pdf_mesclado.append(arquivo1)
pdf_mesclado.append(arquivo2)

# Salvar o nosso pdf
with Path("C:/Users/LUCIANO/Desktop/---Python---Margeylson/zzz_projetos/projeto_margeylson/paginas_pdf/Arquivo_mesclado.pdf").open(mode='wb') as arquivo_final:
    pdf_mesclado.write(arquivo_final)
'''


'''
# Inserir arquivo no meio do outro

# Cria uma lista para mesclar os arquivos
pdf_mesclado = pyf.PdfMerger()

# Passa o nome dos arquivos e seu local para as variáveis
arquivo1 = "MGLU_ER_3T20_POR.pdf"
arquivo2 = "MGLU_ER_4T20_POR.pdf"

# adciona um arquivo na "lista" do PdfMerger
pdf_mesclado.append(arquivo1)

# adciona outro arquivo dps da pagina informada do arquivo ja existente nessa variável
pdf_mesclado.merge(1, arquivo2)

# Salvar o nosso pdf
with Path("C:/Users/LUCIANO/Desktop/---Python---Margeylson/zzz_projetos/projeto_margeylson/paginas_pdf/Arquivo_merger.pdf").open(mode='wb') as arquivo_final:
    pdf_mesclado.write(arquivo_final)
'''


'''
# Rodar as paginas de um pdf em algum angulo específico

# escolhe qual arquivo voce quer alterar
arquivo = "MGLU_ER_3T20_POR.pdf"

# lendo o arquivo e armazenando na variável pdf_rodar
pdf_rodar = pyf.PdfReader(arquivo)

# cria um arquivo pdf vazio
pdf_final = pyf.PdfWriter()
# percorrendo cada pagina do pdf
for pagina in pdf_rodar.pages:

    # rotacionando as páginas no angulo fornecido
    pagina.rotate(90)

    # apos rotacionar as paginas adiciono elas no arquivo pdf final pra poder gerar outro pdf sem modificar o original
    pdf_final.add_page(pagina)

# Salvar o nosso pdf
with Path("C:/Users/LUCIANO/Desktop/---Python---Margeylson/zzz_projetos/projeto_margeylson/paginas_pdf/Arquivo_rotacionado.pdf").open(mode='wb') as arquivo_final:
    pdf_final.write(arquivo_final)

'''



'''
# Trabalhando com Textos - Informações dentro do Pdf

# pegando nome do arquivo
nome_arquivo = "MGLU_ER_4T20_POR.pdf"

# lendo e armazenando arquivo
arquivo = pyf.PdfReader(nome_arquivo)

# pegando numero de paginas que existe no arquivo
num_paginas = len(arquivo.pages)

# pegando varias informações sobre o arquivo e armazenando em um dict
informacoes = arquivo.metadata

# o que estamos procurando nas paginas
texto_procurado = """| Despesas com Vendas""" # necessário encontrar um padrão desse texto específico dentro do arquivo, para que a busca seja mais seletiva

# percorrendo cada pagina para procurar esse texto
for i, pagina in enumerate(arquivo.pages,start=1):
    
    # pegando o que esta escrito nessa pagina  e verificando se o que estamos procurando esta dentro dela
    texto_da_pagina = pagina.extract_text()
    if texto_procurado in texto_da_pagina:
        # informa em que pagina esta esse texto
        print(f"Está na página {i}")
        # armazenar as infos que quero ja que encontrei a página com o texto fornecido
        num_pagina = i
        texto_final = texto_da_pagina
        break


# tratando o texto a antes de pegar o que quero de fato
texto_final = texto_final.replace("   ", " ")
texto_final = texto_final.replace("  "," ")
texto_final = texto_final.replace("\n \n ", "&&&&&")
texto_final = texto_final.replace("\n","")
texto_final = texto_final.replace("&&&&&", "\n")


# pegando a posição do indice da string em que o texto procurado esta
posicao = texto_final.find("| Despesas com Vendas")
# pegando a até qual posição o texto acima vai pra podermos extrair ele corretamente
posicao_final = texto_final.find("|", posicao + 1)
texto_despesas = texto_final[posicao:posicao_final]
print(texto_despesas)


'''



'''

# lendo tabelas de pdf

#df = dataframe(tabelas dentro do python se chamam dataframe)

df = tabula.read_pdf("MGLU_ER_3T20_POR.pdf", pages = 5) # lendo a tabela que esta na pagina cinco e armazenando nessa variavel, o tabula retorna uma lista com todas as tabelas na pagina que esta procurando


# pegando a tabela dessa lista de tabelas encontrada nesse pagina 
tabela = df[0] 


# tratando os erros presentes na tabela como linhas e colunas vazias ou titulos inexistentes
tabela = tabela.dropna(how='all')# excluindo todas linhas vazias
tabela = tabela.dropna(how='all', axis=1) # excluindo todas as colunas vazias
tabela.columns = tabela.iloc[0] # transforma a linha de índice 0 em titulos para as colunas
tabela = tabela.drop(tabela.index[0]) # exclui a primeira linha ja que ela virou título para nossas colunas
tabela = tabela.reset_index(drop = True)# colocar o índice das linhas começando do 0 em diante
# tabela.to_excel("nomedoarquivo.xlsx") caso queria transformar essa tabela em excel

# depois de tratada mostra a tabela na tela
print(tabela)

'''



'''
# as vezes podem existir mais de uma tabela na mesma página
df = tabela.read_pdf("MGLU_ER_3T20_POR.pdf", pages = 12)
# por isso é necessário um for para percorrer a lista de tabelas que é retornada
for tabela in df:
    # e dentro de cada tabela você faz os mesmos tratamentos ja mostrados acima
    tabela = tabela.dropna(how='all')# excluindo todas linhas vazias
    tabela = tabela.dropna(how='all', axis=1) # excluindo todas as colunas vazias
    # e depois mostra elas na tela separadamente
    print(tabela)

'''



'''

# pra caso der merda na hora de ler as tabeas no pdf e o tabula não conseguir ler direito ou faltar informações
df = tabela.read_pdf("MGLU_ER_3T20_POR.pdf", pages = 12, lattice = True) # esse outro parâmetro diz ao tabula pra ler a tabela de forma diferente, pra que ele consiga assim extrair mais informações, porem elas vão precisar ser mais bem tratadas.and

# armazena a tabela , retirando ela da lista retornada pelo tabula
tabela = df[0]

tabela = tabela.dropna(how='all')# excluindo todas linhas vazias
tabela = tabela.dropna(how='all', axis=1) # excluindo todas as colunas vazias

titulo_tabela = tabela.iloc[0] # pega o título dessa tabela
titulo_tabela = titulo_tabela.dropna() # retira linhas vazias

tabela.columns = titulo_tabela # muda o título da tabela depois de tratarmos ele

print(tabela) # ao final de todos tratamentos printamos a tabela final

'''



# Captando imagens de um arquivo pdf
'''
nome_arquivo = "MGLU_ER_3T20_POR.pdf"
arquivo = Pdf.open(nome_arquivo)

n_arquivo = 0

for i, pagina in enumerate(arquivo.pages):
    for nome, imagem in pagina.images.items():
        imagem_para_salvar = PdfImage(imagem)
        imagem_para_salvar.extract_to(fileprefix=f'imgs/Pagina_{i:02}_{n_arquivo}')
        n_arquivo += 1

'''
# acho que dps de ler todos esses códigos e explicações eu nâo preciso comentar esse código acima né
