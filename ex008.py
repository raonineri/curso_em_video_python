# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

distancia_m = float(input("Digite uma distância em metros: "))
print('-=' * 10)

print(f'{distancia_m}m corresponde a:')
print('-=' * 10)
print(f'{distancia_m/1000} Km\n'
      f'{distancia_m/100} Hm\n'
      f'{distancia_m/10} Dam\n'
      f'{distancia_m*10} Dm\n'
      f'{distancia_m*100} Cm\n'
      f'{distancia_m*1000} mm')
print('-=' * 10)
