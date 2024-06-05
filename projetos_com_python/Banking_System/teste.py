import os
import openpyxl
from openpyxl import workbook

book = openpyxl.load_workbook(filename= 'Projetos_com_python/Banking_System/Banco_de_Dados.xlsx')


nome = 'Ana'
ws = workbook
sheet_selecionada = book['Sheet1']
#print(len(sheet_selecionada["A"]))


    