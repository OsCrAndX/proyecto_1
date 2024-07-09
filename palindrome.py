"""
Find a palindrome word.
"""


############ CASO 1 ##############

palabra_usuario = input("Ingrese una palabra para verificar si el palindroma: ")

palabra_usuario = palabra_usuario.lower()

palabra_2 = list(palabra_usuario)

palabra_2.reverse()

palabra_2 = "".join(palabra_2)

if palabra_usuario == palabra_2:
    print("La palabra es palíndroma. ¡Felicitaciones!")
else:
    print("La palabra no es palíndroma")


#####################################
############ CASO 2 ##############

# palabra_usuario = input("Ingrese una palabra para verificar si el palindroma: ")

# palabra_usuario = palabra_usuario.lower()

# palabra_invertida = palabra_usuario[::-1]

# if palabra_usuario == palabra_invertida:
#     print("La palabra es palindroma")
# else:
#     print("La palabra no es palindroma")