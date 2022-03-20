largura = float(input('Digite a Largura da sua parede'))
altura = float(input('Digite a altura da sua parede'))
area = largura * altura

somando_2 = ("Sua parede  tem a dimensão de {} x {} e sua área  é de {}m2".format(largura,altura,area))
tinta = area / 2
print(somando_2)
print("Para pintar a sua parede serão necessários {}l de tinta".format(tinta))
