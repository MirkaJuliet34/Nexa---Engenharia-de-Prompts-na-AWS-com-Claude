# Descrição
# A engenharia de prompts é essencial para obter respostas precisas e relevantes de modelos de linguagem. Boas práticas incluem a clareza, a especificidade e a contextualização dos prompts. Com base nisso, complete o código deste desafio, associando as boas práticas de engenharia de prompts com suas respectivas descrições.

# Entrada
# A entrada consiste na boa prática de engenharia de prompts para a qual você deve retornar a descrição. Neste contexto, as seguintes boas práticas são consideradas válidas para este desafio de código:

#"Clareza"
#"Especificidade"
#"Contextualização"
#"Iteração"
# Saída
# A saída esperada é a descrição associada à boa prática fornecida como entrada. Seguem as saídas possíveis, listadas aleatoriamente, para que você possa analisar e associar corretamente:

#"Fornecer detalhes específicos para evitar ambiguidades"
#"Ajustar o prompt com base no feedback recebido"
#"Usar linguagem clara e direta"
#"Incluir contexto relevante para guiar a resposta"
# Exemplos
# A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

# Entrada	Saída
# Clareza	Usar linguagem clara e direta
# Especificidade	Fornecer detalhes específicos para evitar ambiguidades
# Contextualização	Incluir contexto relevante para guiar a resposta

# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input()

# Função responsável por receber uma prática e retornar sua respectiva descrição.
def identificar_pratica(pratica):
    if pratica == "Especificidade":
        return "Fornecer detalhes específicos para evitar ambiguidades"
    elif pratica == "Iteração":
        return "Ajustar o prompt com base no feedback recebido"
    elif pratica == "Clareza":
        return "Usar linguagem clara e direta"
    elif pratica == "Contextualização":
        return "Incluir contexto relevante para guiar a resposta"
    else:
        return "Boa prática não encontrada"

print(identificar_pratica(entrada))
