valor = int(input('Valor em reais: '))

valor_cem = valor / 100
valor_cinquenta = (valor % 100) / 50
valor_vinte = ((valor % 100) % 50) / 20
valor_dez = (((valor % 100) % 50) % 20 ) / 10
valor_cinco = ((((valor % 100) % 50) % 20 ) % 10) / 5
valor_dois = (((((valor % 100) % 50) % 20 ) % 10) / 5) / 2
valor_um = (((((valor % 100) % 50) % 20 ) % 10) / 5) % 2

print('%d nota(s) de R$100,00 ' %(valor_cem))
print('%d nota(s) de R$50,00 ' %(valor_cinquenta))
print('%d nota(s) de R$20,00 ' %(valor_vinte))
print('%d nota(s) de R$10,00 ' %(valor_dez))
print('%d nota(s) de R$5,00 ' %(valor_cinco))
print('%d nota(s) de R$2,00 ' %(valor_dois))
print('%d nota(s) de R$1,00 ' %(valor_um))
