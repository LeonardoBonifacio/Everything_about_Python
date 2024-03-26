from elemento import Elemento

primeiro = ultimo = None

while True:
    vl = int(input('Valor ou -1 para encerrar: '))
    if vl != -1:
        novo = Elemento(vl)
        if primeiro == None:
            primeiro = novo
            ultimo = novo
        else:
            ultimo.ligaCom(novo)
            ultimo = novo
    else:
        if primeiro !=  None:
            aux = primeiro
            while aux:
                print(f'{aux}', end=' --> ')
                aux = aux.retornaLigacao()
            print("Null")
        break
