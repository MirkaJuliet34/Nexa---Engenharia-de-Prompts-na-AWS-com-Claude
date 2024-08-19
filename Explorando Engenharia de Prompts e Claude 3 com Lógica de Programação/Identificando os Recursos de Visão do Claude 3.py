# Além de suas habilidades de processamento de texto, Claude 3 também pode trabalhar com imagens, permitindo uma variedade de tarefas relacionadas à visão. Com base nisso, complete o código deste desafio, associando os recursos de visão do Claude 3 com suas respectivas descrições.

# Saiba mais em: Claude da Anthropic no Amazon Bedrock, e conheça os casos de uso e recursos na Documentação da Anthropic.

# Entrada
# A entrada consiste no recurso de visão do Claude 3 para o qual você deve retornar a descrição. Neste contexto, os seguintes recursos são considerados válidos para este desafio de código:

# "Extrair dados de imagens"
# "Identificar objetos em imagens"
# "Esclarecer dúvidas sobre imagens"
# "Traduzir textos em imagens"
# Saída
# A saída esperada é a descrição associada ao recurso fornecido como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente:

# "Converter texto presente em imagens para outro idioma"
# "Analisar e identificar objetos específicos em imagens"
# "Fornecer respostas a perguntas sobre o conteúdo da imagem"
# "Obter e estruturar dados visuais de imagens"
# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Entrada	Saída
# Extrair dados de imagens	Obter e estruturar dados visuais de imagens
# Identificar objetos em imagens	Analisar e identificar objetos específicos em imagens
# Esclarecer dúvidas sobre imagens	Fornecer respostas a perguntas sobre o conteúdo da imagem

# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber um recurso de visão e retornar sua respectiva descrição.
def identificar_recurso_visao(recurso):
    if recurso == "Extrair dados de imagens":
        return "Obter e estruturar dados visuais de imagens"
    elif recurso == "Identificar objetos em imagens":
        return "Analisar e identificar objetos específicos em imagens"
    elif recurso == "Esclarecer dúvidas sobre imagens":
        return "Fornecer respostas a perguntas sobre o conteúdo da imagem"
    elif recurso == "Traduzir textos em imagens":
        return "Converter texto presente em imagens para outro idioma"
    else:
        return "Recurso não encontrado"

print(identificar_recurso_visao(entrada))

