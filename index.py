import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from openpyxl import load_workbook
import os

def criar_carregar():
    planilha = "Minhas_Contas.xlsx" 
    if os.path.exists(planilha):
        return pd.read_excel (planilha, usecols=["Tipo","Descricao","Categoria", "Valor", "Vencimento", "Status"])
    else:
        return pd.DataFrame(columns=["Tipo","Descricao","Categoria", "Valor", "Vencimento", "Status"])
    

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

    categorias={"Saidas":['Transporte','Lazer','Investimento','Fixo','NaN'],"Entradas":['Pagamentos','Presentes','Rendimentos']}

    df= criar_carregar()

    tipo=int(input("Qual o tipo do valor?\n"
                   "[1] Entrada\n"
                   "[2] Saida\n"
                   "Escolha: "))
    
    desc = input("Descrição (ex: Gasolina): ").capitalize()

    if tipo == 1:
        tipo='Entrada'
        categ_salva=categorias['Entradas']
        for n, c in enumerate(categorias["Entradas"]):
            print(f'{n+1} - {c}')

    elif tipo == 2:
        tipo='Saida'
        categ_salva=categorias['Saidas']
        for n, c in enumerate(categorias["Saidas"]):
            print(f'{n+1} - {c}')

    while True:
        try:
            categ= int(input("Escolha a categoria: "))
            if len(categ_salva)< categ or categ <=0:
                print(f"Erro: Escolha um número entre 1 e {len(categ_salva)}")
                continue 
            break
        except:
            print("Opção Inválida! Somente números de [1 á 5].")

    categ_salva=categ_salva[categ-1]

    while True:
        try:
            valor = float(input("Valor (ex: 150.00): ")) 
            break
        except:
            print("Opção Inválida! Somente números.")

    data=tratar_data()

    status = input("Status (Pago/Pendente): ").lower().capitalize()
            

    nova_linha={
        'Tipo':tipo,
        'Descricao':desc,
        'Categoria':categ_salva,
        'Valor':valor,
        'Vencimento':data,
        'Status':status
    }

    df = df._append(nova_linha, ignore_index=True)
    df.to_excel("Minhas_Contas.xlsx", index=False, engine='openpyxl')
    mostrar_grafico=(input("Você quer ver um gráfico sobre as contas?\n" \
    "[1] - Gráfico de gastos por setor\n"
    '[2] - Gráfico de Gastos Gerais\n' \
    '[3] - Balanço Mensal (lucro ou Prejuizo)\n'
    'Escolha [Deixe em branco para não ver]: '))
    if mostrar_grafico != '':
        mostrar_grafico= int(mostrar_grafico)
        if mostrar_grafico == 1:
            grafico_gastos_setor(df)
        elif mostrar_grafico ==2:
            grafico_gastos_gerais(df)
        elif mostrar_grafico==3:
            grafico_lucro(df)
    else:
        print("Opção inválida! Prosseguindo...")
        
    formatar()

def grafico_gastos_gerais(df):
    
    df['Vencimento']= pd.to_datetime(df['Vencimento'])
    gastos_pagos=df[df['Status']=='Pago']['Valor'].sum()
    gastos_pendentes=df[df["Status"]=='Pendente']['Valor'].sum()
    categories=['Pago','Pendente']
    values=[gastos_pagos,gastos_pendentes]
    plt.bar(categories, values, color=['green','red'])
    plt.title("Status das Contas - Janeiro 2026")
    plt.ylabel('Valor (R$)')
    plt.show()

def grafico_gastos_setor(df):
    if df.empty:
        return
    soma_por_categoria= df.groupby('Categoria')["Valor"].sum()
    plt.figure()
    soma_por_categoria.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Gastos Por Setor")
    plt.ylabel('')
    plt.show()

def grafico_lucro(df):
    if df.empty:
        return
    soma_entrada=df[df['Tipo'] == 'Entrada']['Valor'].sum()
    soma_saida=df[df['Tipo'] == 'Saida']['Valor'].sum()
    saldo=soma_entrada-soma_saida
    nome=['Entradas','Saídas']
    valores=[soma_entrada,soma_saida]
    plt.figure(figsize=(6,5))
    plt.bar(nome,valores,color=["green", 'red'])
    if saldo >= 0:
        cor_saldo = 'green'
        texto_saldo = f"LUCRO: R$ {saldo:.2f}"
    else:
        cor_saldo = 'red'
        texto_saldo = f"PREJUÍZO: R$ {saldo:.2f}"
    plt.title(f"Balanço do Mês\n{texto_saldo}",color=cor_saldo,fontweight='bold')

    plt.ylabel('Valor (R$)')
    plt.show()

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

