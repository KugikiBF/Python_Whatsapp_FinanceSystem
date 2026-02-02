import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from openpyxl import load_workbook
import os

def criar_carregar():
    planilha = "Minhas_Contas.xlsx" 
    if os.path.exists(planilha):
        return pd.read_excel (planilha, usecols=["Descricao","Categoria", "Valor", "Vencimento", "Status"])
    else:
        return pd.DataFrame(columns=["Descricao","Categoria", "Valor", "Vencimento", "Status"])
    

def tratar_data():
    data = input("Vencimento (pode ser 25/01/2026, 25-01-2026 ou 25012026): ")

    data_limpa = data.replace("-", "").replace("/", "").replace(".", "")
    if len(data_limpa) != 8:
        print("Data estranha... Tente digitar 8 números (DDMMAAAA).")
        return tratar_data() 
    
    dia = data_limpa[:2]   
    mes = data_limpa[2:4]  
    ano = data_limpa[4:]   
    
    data_corrigida = f"{ano}-{mes}-{dia}"
    return data_corrigida

def adicionar_gasto():


    df= criar_carregar()
    desc = input("Descrição (ex: Gasolina): ").capitalize()
    categ= input("Categorias:\n" \
    "1 - Transporte\n"
    "2 - Lazer\n"
    "3 - Investimento\n"
    "4 - Fixo\n"
    "Escolha: ")
    valor = float(input("Valor (ex: 150.00): ")) 
    data=tratar_data()
    status = input("Status (Pago/Pendente): ").lower().capitalize()

    nova_linha={
        'Descricao':desc,
        'Categoria':categ,
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
    ws.column_dimensions['C'].width = 15
    ws.column_dimensions['D'].width = 20
    wb.save(planilha)


while True:
    continuar=int(input("[1] Para Adicionar\n"
    "[2] Para Sair\n"
    "Escolha: "))
    if continuar == 1:
        adicionar_gasto()
    elif continuar == 2:
        print('Saindo...')
        break
    else:
        print("Erro: Escolha inválida")

