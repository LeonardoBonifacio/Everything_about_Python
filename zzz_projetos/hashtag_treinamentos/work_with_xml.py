import xmltodict # transforma xml em dicionários python
import pandas as pd # trabalhar com tabelas e dados de uma forma geral
import os # lida com arquivos e pastas da nossa máquina assim como o pathlib
import xml.etree.ElementTree as ET # pra criar a estrutra de arvore do xml


# criando uma função pra so passar o nome do arquivo xml/DANFE a ser lido e tratado
def ler_xml_danfe(nota):
    # abre e fecha um arquivo no modo forncecido(w, r, a, b) com o nome do arquivo ou caminho passado
    with open(f'zzz_projetos/hashtag_treinamentos/xml/{nota}', 'rb') as arquivo:
        documento = xmltodict.parse(arquivo) # trasnformando o arquivo xml aberto em um dict

    '''
    # pegando varias informações passando o caminho em arvore do xml(convertido em um dict)
    print(documento['nfeProc']['NFe']['infNFe']['dest']['xNome'])
    print(documento['nfeProc']['NFe']['infNFe']['emit']['xFant'])
    '''


    # pra não ter que ficar passando o caminho inteiro do dicionário a todo momento e ja que ja sabemos que todas as informações que nos prcisamos estão agregados em um mesmo caminho do dicionário, passamos o caminho pra uma variável para ficar menos verboroso quando estivermos buscando as informações
    dic_notafiscal = documento['nfeProc']['NFe']['infNFe']


    '''
    # caso n tenha acesso a leitura bonitinha em arvore do arquivo xml, será necessário ir percorrendo cada chave do dict com um for e verificando que outras chaves e valores estão dentro dele
    nome = ''
    for item in dic_notafiscal['emit']['xNome']:
        nome += item
        # item nesse caso era cada letra do nome da empresa, por isso juntei as letras em uma variável pra poder 'formar o nome'
    print(nome)

    '''
    # pegando o valor total da nota fiscal
    valor_total = dic_notafiscal['total']['ICMSTot']['vNF']

    # pegando o cnpj de quem vendeu
    cnpj_vendedor = dic_notafiscal['emit']['CNPJ']

    # pegando o nome de quem vendeu
    nome_vendedor = dic_notafiscal['emit']['xNome']

    # pegando o cpf de quem comprou
    cpf_comprador = dic_notafiscal['dest']['CPF']

    # pegando o nome de quem comprou
    nome_comprador = dic_notafiscal['dest']['xNome']

    # pegando todos os produtos,seus nomes e valores e os colocando em uma lista de tuplas
    lista_produtos = []
    produtos = dic_notafiscal['det'] # det contem 7 produtos
    for produto in produtos:
        valor_produto = produto['prod']['vProd']
        nome_produto = produto['prod']['xProd']
        lista_produtos.append((nome_produto, valor_produto))



    # criando um dicionário com as informacões obtidas, para melhorar a visualização e poder integrar com o pandas
    resposta = {'Valor Total':         [valor_total],
                'CNPJ de Quem Vendeu': [cnpj_vendedor],
                'Nome de Quem Vendeu': [nome_vendedor],
                'CPF do Comprador':    [cpf_comprador],
                'Nome do Comprador':   [nome_comprador], 
                'Produtos' :           [lista_produtos]
            }
    # fiz todos os valores de cada chave do dicionario se transformarem um lista para o pandas entender que ao converter para xlsx eu quero que todas as informações desse dict fiquem em apenas uma linha, já que se trata de uma nota fiscal
    return resposta



# criando outra função pra so passar o nome do arquivo xml/SERVIÇOS a ser lido e tratado
# é necessário criar outras funções para tipos de notas/arquivos xml diferentes pois cada um tem um padrão de caminhos a serem seguidos, que dão acesso a suas informações
def ler_xml_servicos(nota):
    # abre e fecha um arquivo no modo forncecido(w, r, a, b) com o nome do arquivo ou caminho passado
    with open(f'zzz_projetos/hashtag_treinamentos/xml/{nota}', 'rb') as arquivo:
        documento = xmltodict.parse(arquivo) # trasnformando o arquivo xml aberto em um dict

    # pra não ter que ficar passando o caminho inteiro do dicionário a todo momento e ja que ja sabemos que todas as informações que nos prcisamos estão agregados em um mesmo caminho do dicionário, passamos o caminho pra uma variável para ficar menos verboroso quando estivermos buscando as informações
    dic_notafiscal = documento['ConsultarNfseResposta']['ListaNfse']['CompNfse']['Nfse']['InfNfse']

    # pegando o valor total da nota fiscal
    valor_total = dic_notafiscal['Servico']['Valores']['ValorServicos']

    # pegando o cnpj de quem vendeu
    cnpj_vendedor = dic_notafiscal['PrestadorServico']['IdentificacaoPrestador']['Cnpj']

    # pegando o nome de quem vendeu
    nome_vendedor = dic_notafiscal['PrestadorServico']['RazaoSocial']

    # pegando o cpf de quem comprou
    cpf_comprador = dic_notafiscal['TomadorServico']['IdentificacaoTomador']['CpfCnpj']['Cnpj']

    # pegando o nome de quem comprou
    nome_comprador = dic_notafiscal['TomadorServico']['RazaoSocial']

    # pegando os serviços prestados para essa nota fiscal
    servicos = dic_notafiscal['Servico']['Discriminacao'] # det contem 7 produtos

    # criando um dicionário com as informacões obtidas, para melhorar a visualização e poder integrar com o pandas
    resposta = {'Valor Total':         [valor_total],
                'CNPJ de Quem Vendeu': [cnpj_vendedor],
                'Nome de Quem Vendeu': [nome_vendedor],
                'CPF do Comprador':    [cpf_comprador],
                'Nome do Comprador':   [nome_comprador], 
                'Produtos' :           [servicos]
            }
    # fiz todos os valores de cada chave do dicionario se transformarem um lista para o pandas entender que ao converter para xlsx eu quero que todas as informações desse dict fiquem em apenas uma linha, já que se trata de uma nota fiscal
    return resposta


# criando uma lista dos arquivos encontrados no caminho passado como parametro do listdir
lista_arquivos = os.listdir('zzz_projetos/hashtag_treinamentos/xml/')

# percorrendo cada arquivo encontrdo e verificando tanto se ele é um xml, se for verifica qual tipo de nota fiscal é e chama a sua devida função para tratar cada tipo de arquivo xml/notaFiscal
for arquivo in lista_arquivos:
    if 'xml' in arquivo:
        if 'DANFE' in arquivo:
            print(ler_xml_danfe(arquivo))
            print()
        else: # se n é uma DANFE é uma nota de serviços
            print(ler_xml_servicos(arquivo))
            print()

'''
# caso queria que as notas fiscais acima fiquem mais visiveis de serem lidas, basta criar um DataFrame(que é basicamente uma tabela) com o pandas e ou visualizar essa tabela pelo próprio terminal ou visualizar em um arquivo xlsx(excel) com a estrutura.to_excel abaixo que cria um arquivo xlsx baseado na tabela passada a ele
tabela = pd.DataFrame.from_dict(resposta)
print(tabela)
tabela.to_excel('NFs.xlsx')
'''

'''
# exemplo pra criar extrutura de arvore do xml
root = ET.Element("TODOS_ERROS") # cria a tag raiz do xml
erro_element = ET.SubElement(root,'Erro')# cria uma subtag pra por dentro da raiz
erro_element.text = f"\nErro: {erro}\nData: {data}\n" # inseri texto nessa subtag
tree = ET.ElementTree(root) # cria a estrutura completa baseada no que fizemos acima
tree.write(random.choice(NOMES_ERROS), encoding='utf-8') # escreve o nome do arquivo(baseado numa randomização de nomes dentro de uma lista) e classifica as estruturas das tags como utg-8 pra n dar problema com caracteres especias, e por fim cria o arquivo
print('...Arquivo xml com erro ocorrido criado, por favor encerre o programa e verifique o erro...')
'''




