from math import hypot #Math é a biblioteca que usamos para realizar operações aritiméticas mais complexas.import
                       #hypot é a parte da biblioteca, que realiza calcullos de Hipotenusa.
co = float(input('Comprimento cateto oposto'))
ca = float(input('Comprimento cateto adjacente'))
hi = hypot(co,ca)
print('A hipotenusa vai medir {}'.format(hi))