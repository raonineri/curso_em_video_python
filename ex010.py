# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar


num = float(input("Quanto dinheiro você tem na carteira? R$ "))

dolar = 5.21
euro = 6.14

print(f"Você tem R$ {num}")

print(f'Este valor equivale a € {num/euro:.2f} ou a $ {num/dolar:.2f}.')

