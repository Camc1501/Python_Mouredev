### Listas ###

numero=12345764456
numero_str=str(numero)
resultado= 0
flag = True

while flag:
    for element in str(numero):
        resultado += int(element)
    if len(str(resultado))==1:
        flag = False
    

print(len(numero_str))
print(numero)
print(resultado)
