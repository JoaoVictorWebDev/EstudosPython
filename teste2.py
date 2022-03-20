import openpyxl
book = openpyxl.load_workbook('vagoes.xlsx')

#Escolher página para editar

Funcionarios = book["Funcionarios"]
#imprimindo os dados de cada linha
for  rows in Funcionarios.iter_rows(min_row =1,max_row = 2 ):
 for cell in rows:
    print(cell.value)