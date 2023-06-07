### Operadores ###

### Aritméticos ###
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(10 / 3)
print(10 % 3) # Modulo -> es lo que sobra de la división
print(10 // 3) # Floor division -> división aproximada
print(2 ** 3) # Exponente

print("Hola" + "Python" + "¿Que tal?") # + También une cadenas de texto 

print("Hola" + str(5))# no se puede combianr tipos de datos para imprimir, se debe castear

print("Hola " * 5)
 

 ### Comparativos ###
print("Comparativos")
print(3 > 4)
print(3 < 4)
print(3 <= 4)
print(3 >= 4)
print(3 == 4)
print(3 != 4)

print("Comparativos2")
print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Bola")
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")
#al comparar strings se comprueba una ordenación alfabética por ASCII


### Operadores Lógicos ###
print("### Operadores Lógicos")
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not(3 > 4))