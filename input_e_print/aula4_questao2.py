F = float(input('Temperatura em Fahrenheit: ')) #recebendo o valor em fahrenheits
C = (F -32) * (5/9) #conversão para Celsius

C = int(C) # conversão de float para int

print('%.0f graus Fahrenheit são %d graus Ceusius' % (F,C))

