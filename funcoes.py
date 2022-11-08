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