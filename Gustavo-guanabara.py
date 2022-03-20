#verificação de senha Estudo 31/01/2002
senha_inserir = input('Digite uma senha')
confirmaçao_senha=input('Digite a senha novamente')

if senha_inserir != confirmaçao_senha:
    print('Digite novamente')
else:print('Logado com sucesso')