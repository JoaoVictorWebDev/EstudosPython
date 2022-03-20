nome = str(input('Digite seu nome ')).strip() # <<<<< Corta os espaços presentes numa variavel

print('Seu nome em maisculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome tem  {} LETRAS'.format(len(nome)))