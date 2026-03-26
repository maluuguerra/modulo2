prud1 = input('Digite o nome do produto 1 : ')
preco1 = float(input('Digite o preço do produto 1 : '))
quant1 = int(input('Digite a quantidade do produto 1 :'))
total1 = preco1 * quant1

prud2 = input('Digite o nome do produto 2 : ')
preco2 = float(input('Digite o preço do produto 2 : '))
quant2 = int(input('Digite a quantidade do produto 2 :'))
total2 = preco2 * quant2


prud3 = input('Digite o nome do produto 3 : ')
preco3 = float(input('Digite o preço do produto 3 : '))
quant3 = int(input('Digite a quantidade do produto 3 :'))
total3 = preco3 * quant3

total = total1 + total2 + total3

print(f'Total: R${total: ,.2f}')



