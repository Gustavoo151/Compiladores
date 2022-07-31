lista = [3,9,1,6,4,1,2]
arvore = []
contador = 0

for c in range(len(lista)):

    if contador == len(lista):
            break

    elif len(arvore) == 0:
        arvore.append(f'Primeiro no: {lista[contador]}')

    elif lista[contador] > lista[contador + 1]:
        arvore.append(f'Menor: {lista[contador + 1]}')
        contador += 1

    elif lista[contador] == lista[contador + 1]:
        arvore.append(f'Igual: {lista[contador + 1]}')

    elif lista[contador] < lista[contador + 1]:
        arvore.append(f'Maior: {lista[contador + 1]}')
        contador += 1
    
for c in range(len(arvore)):
    print(arvore[c])