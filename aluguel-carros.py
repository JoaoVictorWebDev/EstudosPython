dias = int(input('O carro foi alugado por quantos dias?'))
km = float(input('Quantos Km foram rodados?'))
pago = dias *60 + km * 0.5
print('O total a pagar é de {}R$'.format(pago))