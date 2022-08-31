# Lukas Jacon Barboza
"""
Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  fazer  um  programa,  usando  a linguagem de programação que desejar, que seja capaz de validar expressões de lógica propisicional escritas em latex e definir se são expressões gramaticalmente corretas. Você validará apenas a forma da expressão (sintaxe).
A entrada será fornecida por um arquivo de textos que será carregado em linha de comando,
com a seguinte formatação:
1. Na primeira linha deste arquivo existe um número inteiro que informa quantas expressões lógicas estão no arquivo.
2. Cada uma das linhas seguintes contém uma expressão lógica que deve ser validada.
A saída do seu programa será no terminal padrão do sistema e constituirá de uma linha de saída para cada expressão lógica de entrada contendo ou a palavra valida ou a palavra inválida e nada mais.
Gramática:
        Formula=Constante|Proposicao|FormulaUnaria|FormulaBinaria.
        Constante="T"|"F".
        Proposicao=[a−z0−9]+
        FormulaUnaria=AbreParen OperadorUnario Formula FechaParen
        FormulaBinaria=AbreParen OperatorBinario Formula Formula FechaParen
        AbreParen="("
        FechaParen=")"
        OperatorUnario="¬"
        OperatorBinario="∨"|"∧"|"→"|"↔"
Cada  expressão  lógica  avaliada  pode  ter  qualquer  combinação  das  operações  de  negação, conjunção, disjunção, implicação e bi-implicação sem limites na combiação de preposições e operações.
Os valores lógicos True e False estão representados na gramática e, como tal, podem ser usados em qualquer expressão de entrada.
"""

import os


def QuantidadeParenteses(expressao):
    QuantidadeAberta = QuantidadeFechada = 0
    for simbolo in expressao:
        if VerificaParenteses(simbolo) == 'Abrir':
            QuantidadeAberta += 1
        if VerificaParenteses(simbolo) == 'Fechar':
            QuantidadeFechada += 1
    return QuantidadeAberta - QuantidadeFechada


def Proposicao(simbolo):
    if simbolo.isalpha() and simbolo.lower() == simbolo or simbolo.isnumeric():
        return True
    return False


def Constante(expressao):
    if expressao == 'T' or expressao == 'F':
        return True
    return False


def VerificaParenteses(simbolo):
    if simbolo == ')':
        return 'Fechar'
    elif simbolo == '(':
        return 'Abrir'
    return ''


def VerificaBarra(expressao):
    for i in range(len(expressao)):
        if expressao[i] == '\\':
            return True
    return False


def VerificaEspaco(simbolo):
    if simbolo == ' ':
        return True
    return False


def VerificaOperadores(expressao, i):
    Comprimento_do_Operador = 0
    Tipo_do_Operador = "Binario"
    try:
        if expressao[i + 1] == 'v' and expressao[i + 2] == 'e' and expressao[i + 3] == 'e':
            Comprimento_do_Operador = 3
        elif expressao[i + 1] == 'n' and expressao[i + 2] == 'e' and expressao[i + 3] == 'g':
            Comprimento_do_Operador = 3
            Tipo_do_Operador = "Unario"
        if (expressao[i + 1] == 'w' and expressao[i + 2] == 'e' and expressao[i + 3] == 'd' and
                expressao[i + 4] == 'g' and expressao[i + 5] == 'e'):
            Comprimento_do_Operador = 5
        if (expressao[i + 1] == 'r' and expressao[i + 2] == 'i' and expressao[i + 3] == 'g' and
                expressao[i + 4] == 'h' and expressao[i + 5] == 't' and expressao[i + 6] == 'a' and
                expressao[i + 7] == 'r' and expressao[i + 8] == 'r' and expressao[i + 9] == 'o' and
                expressao[i + 10] == 'w'):
            Comprimento_do_Operador = 10
        if (expressao[i + 1] == 'l' and expressao[i + 2] == 'e' and expressao[i + 3] == 'f' and
                expressao[i + 4] == 't' and expressao[i + 5] == 'r' and expressao[i + 6] == 'i' and
                expressao[i + 7] == 'g' and expressao[i + 8] == 'h' and expressao[i + 9] == 't' and
                expressao[i + 10] == 'a' and expressao[i + 11] == 'r' and expressao[i + 12] == 'r' and
                expressao[i + 13] == 'o' and expressao[i + 14] == 'w'):
            Comprimento_do_Operador = 14
    except:
        return 0, ""
    return Comprimento_do_Operador, Tipo_do_Operador


def VerificaFormula(expressao, i, Tipo_do_Operador):
    Tamanho_da_Formula = -1
    x = ""
    ContadorAberturaParenteses = ContadorFechamentoParenteses = 0
    if Tipo_do_Operador == "Unario":
        if Constante(expressao[i]):
            simbolo = expressao[i + 1]
            if VerificaParenteses(simbolo) == 'Fechar':
                Tamanho_da_Formula += 1
                return True, Tamanho_da_Formula
            else:
                return False, -1

        for j in range(i, len(expressao) - 1):
            if VerificaParenteses(expressao[i]) == 'Abrir':
                if VerificaParenteses(expressao[j]) == 'Abrir':
                    ContadorAberturaParenteses += 1
                elif VerificaParenteses(expressao[j]) == 'Fechar':
                    ContadorFechamentoParenteses += 1
                    if ContadorFechamentoParenteses == ContadorAberturaParenteses:
                        break
            else:
                if VerificaParenteses(expressao[j]) == 'Fechar' and not VerificaEspaco(expressao[j + 1]):
                    break
            x = x + expressao[j]
            Tamanho_da_Formula += 1
    elif Tipo_do_Operador == "Binario":
        for j in range(i, len(expressao)):
            if VerificaParenteses(expressao[i]) == 'Abrir':
                if VerificaParenteses(expressao[j]) == 'Abrir':
                    ContadorAberturaParenteses += 1
                elif VerificaParenteses(expressao[j]) == 'Fechar':
                    ContadorFechamentoParenteses += 1
                    if ContadorFechamentoParenteses == ContadorAberturaParenteses:
                        break
            else:
                if VerificaEspaco(expressao[j]) or VerificaParenteses(expressao[j]) == 'Fechar':
                    break
            x = x + expressao[j]
            Tamanho_da_Formula += 1
    if VerificaParenteses(expressao[i]) == 'Abrir':
        Resultado_da_Expressao = x + ")"
        Tamanho_da_Formula += 1
    else:
        Resultado_da_Expressao = x
    Resultado_da_Formula = VerificaString(Resultado_da_Expressao)
    return Resultado_da_Formula, Tamanho_da_Formula


def VerificaString(expressao):
    Resultado = True
    Tipo_do_Operador = ""
    y = 1

    if QuantidadeParenteses(expressao) != 0:
        return False

    if VerificaBarra(expressao):
        i = 0
        while i < len(expressao):
            simbolo = expressao[i]
            if y == 1:
                if VerificaParenteses(simbolo) != 'Abrir':
                    return False
                y += 1

            elif y == 2:
                Comprimento_do_Operador, Tipo_do_Operador = VerificaOperadores(expressao, i)
                if Comprimento_do_Operador == 0:
                    return False
                i = i + Comprimento_do_Operador
                y += 1

            elif y == 3:
                if not VerificaEspaco(simbolo):
                    return False
                y += 1

            elif y == 4:
                Resultado_da_Formula, Tamanho_da_Formula = VerificaFormula(expressao, i, Tipo_do_Operador)
                i += Tamanho_da_Formula

                if Resultado_da_Formula:
                    if Tipo_do_Operador == "Binario":
                        y += 1
                    elif Tipo_do_Operador == "Unario":
                        return True
                else:
                    return False

            elif y == 5:
                if VerificaEspaco(simbolo):
                    y += 1
                else:
                    return False

            elif y == 6:
                Resultado_da_Formula, Tamanho_da_Formula = VerificaFormula(expressao, i, Tipo_do_Operador)
                i += Tamanho_da_Formula

                if not Resultado_da_Formula:
                    return False
                return True
            i += 1

    else:
        for i in range(len(expressao)):
            ComparaConstante = Constante(expressao)
            ComparaProposicao = Proposicao(expressao[i])

            if not ComparaConstante and not ComparaProposicao:
                return False
    return Resultado


arquivos = os.listdir('textos')
for arquivo in arquivos:
    extensao = os.path.splitext(arquivo)[1]
    if extensao == ".txt":
        with open("textos/%s" % arquivo) as dados:
            nomes = dados.readlines()
            QuantidadePalavras = int(nomes[0])
            contador = 1
    if len(nomes) == QuantidadePalavras + 1:
        contador = 1

        while contador <= QuantidadePalavras:
            palavra = nomes[contador].strip('\n')
            resultado = VerificaString(palavra)
            if resultado:
                print("válida")
            else:
                print("inválida")
            contador += 1
    else:
        print("Número passado nos arquivos txt não condiz com a quantidade de expressões")
