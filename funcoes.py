def transforma_base(lista):
    dicio_final = {}
    for i in range(len(lista)):
        dificuldade = lista[i]['nivel']
        print(dificuldade)
        if dificuldade in dicio_final.keys():
            if lista[i] not in dicio_final.values():
                dicio_final[dificuldade] += [lista[i]]
        if dificuldade not in dicio_final.keys():
            if lista[i] not in dicio_final.values():
                dicio_final[dificuldade] = [lista[i]]
    return dicio_final



def valida_questao(dicio):
    diciofinal = {}
    dicioletras = {}
    count = 0
    soma = 0
    if 'titulo' not in dicio.keys(): 
        diciofinal['titulo'] = 'nao_encontrado'
    if 'nivel' not in dicio.keys():
        diciofinal['nivel'] = 'nao_encontrado'
    if 'opcoes' not in dicio.keys():
        diciofinal['opcoes'] = 'nao_encontrado'
    if 'correta' not in dicio.keys():
        diciofinal['correta'] = 'nao_encontrado'
    if len(dicio.keys())!= 4:
        diciofinal['outro'] ='numero_chaves_invalido'

    if 'titulo' in dicio.keys():
        tit = dicio['titulo'].strip()
        if len(tit) == 0:
            diciofinal['titulo'] = 'vazio'
    
    if 'nivel' in dicio.keys():
        if dicio['nivel']== 'facil':
            count+=1
        if dicio['nivel'] == 'medio':
            count+=1
        if dicio['nivel'] == 'dificil':
            count+=1
        if count!= 1:
            diciofinal['nivel'] = 'valor_errado'
    if 'opcoes' in dicio.keys():
        if len(dicio['opcoes']) !=4:
            diciofinal['opcoes'] = 'tamanho_invalido'

        if len(dicio['opcoes']) ==4:
            for letras, alternativas in dicio['opcoes'].items():
                if 'A' in letras:
                    if 'B' in letras:
                        if 'C' in letras:
                            if 'D' in letras:
                                count+=1
                            else:
                                diciofinal['opcoes'] = 'chave_invalida_ou_nao_encontrada'
                x = alternativas.strip()
                if len(x) == 0:
                    dicioletras[letras] = 'vazia'
    for letra, resp in dicioletras.items():
        if '{}' not in letra or '{}' not in resp:
            diciofinal['opcoes'] = dicioletras
    if 'correta' not in dicio.keys():
        diciofinal['correta'] = 'nao_encontrado'
    if 'correta' in dicio.keys():
        if dicio['correta'] == 'A' or dicio['correta'] == 'B' or dicio['correta'] == 'C' or dicio['correta'] == 'D':
            count+=1
        else:
            diciofinal['correta'] = 'valor_errado'
    return diciofinal


import random
def sorteia_questao(dicio, nivel):
    for dificuldade, questoes in dicio.items():
        if dificuldade == nivel:
            return random.choice(questoes)


import random
def sorteia_questao_inedida(dicio, nivel, lista):
    for dificuldade, questoes in dicio.items():
        if dificuldade == nivel:
            x = random.choice(questoes)
            if x in lista:
                while x in lista:
                    x = random.choice(questoes)
            if x not in lista:
                lista.append(x)
                return x



def questao_para_texto(dicionario, numero):
    saida = '''

----------------------------------------
QUESTAO {}

{}

RESPOSTAS:
A: {}
B: {}
C: {}
D: {}

'''.format(numero, dicionario['titulo'],dicionario['opcoes']['A'], dicionario['opcoes']['B'], dicionario['opcoes']['C'],  dicionario['opcoes']['D']  )

    return saida