from iqoptionapi.stable_api import IQ_Option
import sys
from datetime import datetime, timedelta
from colorama import init, Fore, Back
from time  import time
init(autoreset=True)
API = IQ_Option ('login', 'senha')
API.connect()
if API.check_connect():
    print ('Conectado com Sucesso')
else:
    print('Erro ao Conectar')
    input('\n\n Aperte enter para sair')
    sys.exit()
def cataloga(par, dias,prct_call,prct_put,timeframe):
    data = []
    datas_testadas = []
    sair = False
    time_ = time()
    while sair == False:
        velas = API.get_candles(par,(timeframe * 60),1000,time_)

        for x in velas:
            if datetime.fromtimestamp(x['from']).strftime('%Y-%m-%d') not in datas_testadas:
                datas_testadas.append(datetime.fromtimestamp(x['from']).strftime('%Y-%m-%d'))

                if len(datas_testadas)<= dias :
                    x.update({'cor': 'verde' if x ['open'] < x ['close'] else 'vermelha' if x['open'] >x['close'] else'doji'})
                    data.append(x)
                else:
                    sair = True
                    break
                time_ = int(velas[-1]['from'] -1 )
            analise = {}
            for velas in data:
                horario = datetime.fromtimestamp(velas['from']).strftime('%H:%M')

                if horario not in analise:
                    analise.update({horario: {'verde' : 0 , 'vermelha' : 0 , 'doji' : 0, '%' : 0, 'dir' : ''}})
                    analise[horario] [velas['cor']] += 1
                    try:
                        analise[horario] ['%'] = round(100 * (analise[horario]['verde'] / (analise[horario]['verde']  + (analise[horario]['vermelha'] + ['doji']))))
                    except:
                        pass
    for horario in analise :
     if analise [horario]['%']> 50: analise [horario] ['dir'] = 'CALL'
     if analise[horario]['%'] > 50: analise[horario]['dir'] , analise [horario] ['%']= 'PUT  ',(100 - analise [horario] ['%'])
     return analise

print('\n \n Qual TimeFrame  deseja catalogar', end = '')
timeframe = int(input())

print('\n\n Quantos dias pra analisar?: ', end = '' )
print('\n\n Qual a porcentagem minima?:' , end = '')
porcentagem = int(input())

print('\n\n Testar com quantos martingales:',end='')
martingale = input()
prct_call = abs(porcentagem)
ptct_put = abs(100 - porcentagem)

p = API.get_call_open_time()
print('\n\n')

catalogacao = ()
for par in p['digital']:
    if p['digital'] [par]['open'] == True:
        timer = int(timer())

        print(Fore.GREEN+ '*' + Fore.RESET + 'CATALOGANDO' + par + '...', end='')
        catalogacao.update({par: cataloga(par,dias,prct_call,prct_put,timeframe)})
        print