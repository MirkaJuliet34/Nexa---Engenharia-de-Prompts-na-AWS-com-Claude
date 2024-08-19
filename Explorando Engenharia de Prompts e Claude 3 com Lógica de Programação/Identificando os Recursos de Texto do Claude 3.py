# Claude 3 se destaca no processamento e compreensão de texto, tornando-o uma ferramenta inestimável para inúmeras aplicações. Alguns de seus principais recursos de texto incluem geração de conteúdo, redação e revisão, sumarização, análise e interpretação de texto, entre outros. Com base nisso, complete o código deste desafio, associando os recursos de texto do Claude 3 com suas respectivas descrições.

# Saiba mais em: Claude da Anthropic no Amazon Bedrock, e conheça os casos de uso e recursos na Documentação da Anthropic.

# Entrada
# A entrada consiste no recurso de texto do Claude 3 para o qual você deve retornar a descrição. Neste contexto, os seguintes recursos são considerados válidos para este desafio de código:

# "Geração de conteúdo"
# "Redação e revisão"
# "Sumarização"
# "Análise e interpretação de texto"
# Saída
# A saída esperada é a descrição associada ao recurso fornecido como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente:

# "Sintetizar artigos extensos ou documentos em resumos breves"
# "Oferecer percepções e esclarecer conceitos complexos"
# "Desenvolver conteúdo com base em instruções ou diretrizes"
# "Auxiliar na criação de textos e revisão de materiais escritos"
# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Entrada	Saída
# Geração de conteúdo	Desenvolver conteúdo com base em instruções ou diretrizes
# Redação e revisão	Auxiliar na criação de textos e revisão de materiais escritos
# Sumarização	Sintetizar artigos extensos ou documentos em resumos breves

# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um recurso de texto e retornar sua respectiva descrição.
def identificar_recurso_texto(recurso):
    if recurso == "Geração de conteúdo":
        return "Desenvolver conteúdo com base em instruções ou diretrizes"
    elif recurso == "Redação e revisão":
        return "Auxiliar na criação de textos e revisão de materiais escritos"
    elif recurso == "Sumarização":
        return "Sintetizar artigos extensos ou documentos em resumos breves"
    elif recurso == "Análise e interpretação de texto":
        return "Oferecer percepções e esclarecer conceitos complexos"
    else:
        return "Recurso não encontrado"

print(identificar_recurso_texto(entrada))
