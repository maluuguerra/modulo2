comp = int(input('Informe o comprimento '))  #input para atrubuir o comprimento desejado
larg  = int(input('Informe a largura '))  #input para atrubuir a largura
preco = float(input('Informe o preço do metro quadrado ')) #input para atrubuir o preço


area = comp * larg   #calculo da area em metros quadrados
preco_total = area * preco   # calculo do preço total da area

print('O terreno possui %dm2 e custa  R$%.2f' % (area, preco_total))





