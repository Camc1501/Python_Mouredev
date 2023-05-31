
### Variables ###

my_string_variable = "My String variable"
#CamelCase no se usa.. 
#de las buenas prácticas se hace con _ entre palabras de la variable
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable= str(my_int_variable)#str transforma de int a str
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#Concatenación de variables en un print
print(my_string_variable,my_int_variable,my_bool_variable)
print('Este es el valor de:',my_bool_variable)

#Algunas funciones del Sistema
print(len(my_string_variable))

#Variables en una sola línea
name, surname, alias, age = "Camilo", 'Martínez', 'Camc', 29
print('Me llamo:',name,surname,'Mi edad es:',age,'y mi alias es:',alias)