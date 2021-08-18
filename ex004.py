# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele

variavel = input("Digite algo: ")

print(f"{variavel} é do tipo {type(variavel)}")  # Como o tipo não foi definido no input qualquer valor digitado será
# entendido com do tipo str
print(f"Só é um número? {variavel.isnumeric()}")
print(f"É alfanumérico? {variavel.isalnum()}")
print(f"É composto só por espaços? {variavel.isspace()}")
print(f"Esta escrito com letras maiúsculas? {variavel.isupper()}")
print(f"A primeira letra é maiúscula? {variavel.istitle()}")
