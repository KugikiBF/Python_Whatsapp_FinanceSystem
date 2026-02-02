import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from openpyxl import load_workbook
import os

def criar_carregar():
    planilha = "Minhas_Contas.xlsx" 
    if os.path.exists(planilha):
        return pd.read_excel (planilha, usecols=["Descricao", "Valor", "Vencimento", "Status"])
    else:
        return pd.DataFrame(columns=["Descricao", "Valor", "Vencimento", "Status"])
    

def adicionar_gasto():


    df= criar_carregar()
    desc = input("Descrição (ex: Gasolina): ")
    valor = float(input("Valor (ex: 150.00): ")) 
    data = input("Vencimento (AAAA-MM-DD): ")
    status = input("Status (Pago/Pendente): ")

    nova_linha={
        'Descricao':desc,
        'Valor':valor,
        'Vencimento':data,
        'Status':status
    }

    df = df._append(nova_linha, ignore_index=True)
    df['Vencimento']= pd.to_datetime(df['Vencimento'])


    gastos_pagos=df[df['Status']=='Pago']['Valor'].sum()
    gastos_pendentes=df[df["Status"]=='Pendente']['Valor'].sum()
    categories=['Pago','Pendente']
    values=[gastos_pagos,gastos_pendentes]
    plt.bar(categories, values, color=['green','red'])
    plt.title("Status das Contas - Janeiro 2026")
    plt.ylabel('Valor (R$)')
    plt.show()
    planilha = "Minhas_Contas.xlsx" 
    df.to_excel(planilha, index=False, engine='openpyxl')
    formatar()

def formatar():
    planilha = "Minhas_Contas.xlsx" 
    wb = load_workbook(planilha)
    ws = wb.active
    ws.column_dimensions['A'].width = 30
    ws.column_dimensions['B'].width = 15
    ws.column_dimensions['C'].width = 30
    ws.column_dimensions['D'].width = 15
    wb.save(planilha)




    