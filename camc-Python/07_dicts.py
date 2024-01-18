mi_diccionario = {'1':[],'2':[]}


llaves=['1','2']
valores=[1,2,3,4,5,6,7,8,9,10]

for valor in valores:
    
    for llave in llaves:
        
        if valor%2:
            mi_diccionario[llave].append(valor)
    

print(mi_diccionario)