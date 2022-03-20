import matplotlib.pyplot as plt
import  pandas as pd
ler = pd.read_excel('vagoes.xlsx', sheet_name='Funcionarios')
plt.bar(ler["Idade"],height = 100)
plt.show()