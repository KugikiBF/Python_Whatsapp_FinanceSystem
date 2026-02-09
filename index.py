import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from openpyxl import load_workbook
import os


class ControleFinanceiro:

    def __init__(self,arquivo="Minhas_Contas.xlsx"):
        self.arquivo=arquivo
        self.categorias= {
            "Saidas": ['Transporte', 'Lazer', 'Investimento', 'Fixo', 'Outros'],
            "Entradas": ['Pagamentos', 'Presentes', 'Rendimentos']
        }
        self.df = self._criar_carregar()

    def _criar_carregar(self):
        if os.path.exists(self.arquivo):
            return pd.read_excel (self.arquivo, usecols=["Tipo","Descricao","Categoria", "Valor", "Vencimento", "Status"])
        else:
            return pd.DataFrame(columns=["Tipo","Descricao","Categoria", "Valor", "Vencimento", "Status"])
        

    def _tratar_data(self):
        data = input("Vencimento (pode ser 25/01/2026, 25-01-2026 ou 25012026): ")
        data_limpa = data.replace("-", "").replace("/", "").replace(".", "")
        if len(data_limpa) != 8:
            return self._tratar_data()
            
        dia = data_limpa[:2]   
        mes = data_limpa[2:4]  
        ano = data_limpa[4:]   
        
        data_corrigida = f"{ano}-{mes}-{dia}"
        return data_corrigida

    def adicionar_gasto(self):
        self.df=self._criar_carregar()
        # PEGA O TIPO DE CONTA (ENTRADA/SAIDA)
        while True:
            try:
                tipo=int(input("Qual o tipo do valor?\n"
                    "[1] Entrada\n"
                    "[2] Saida\n"
                    "Escolha: "))
                if tipo == 1 or tipo ==2:
                    break
                else:
                    print("Valor Inválido! Somente 1 ou 2.")
            except:
                print("Valor Inválido! Somente números.")
        # PEGA A CATEGORIA DA CONTA
        if tipo == 1:
            tipo='Entrada'
            categ_salva=self.categorias['Entradas']
            for n, c in enumerate(self.categorias["Entradas"]):
                print(f'{n+1} - {c}')
        elif tipo == 2:
            tipo='Saida'
            categ_salva=self.categorias['Saidas']
            for n, c in enumerate(self.categorias["Saidas"]):
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
        # PEGA A DESCRIÇÃO DA CONTA
        desc = input("Descrição (ex: Gasolina): ").capitalize()
        # PEGA O VALOR DA CONTA
        while True:
            try:
                valor = float(input("Valor (ex: 150.00): ")) 
                break
            except:
                print("Opção Inválida! Somente números.")
        # PEGA O VENCIMENTO DA CONTA
        data=self._tratar_data()
        # PEGA O STATUS DA CONTA
        status = input("Status (Pago/Pendente): ").lower().capitalize()
                

        nova_linha={
            'Tipo':tipo,
            'Descricao':desc,
            'Categoria':categ_salva,
            'Valor':valor,
            'Vencimento':data,
            'Status':status
        }

        self.df = self.df._append(nova_linha, ignore_index=True)
        self.df.to_excel(self.arquivo, index=False, engine='openpyxl')

    def gerar_graficos(self):
        mostrar_grafico=(input("Você quer ver um gráfico sobre as contas?\n" \
        "[1] - Gráfico de gastos por setor\n"
        '[2] - Gráfico de Gastos Gerais\n' \
        '[3] - Balanço Mensal (lucro ou Prejuizo)\n'
        'Escolha [Deixe em branco para não ver]: '))
        if mostrar_grafico != '':
            mostrar_grafico= int(mostrar_grafico)
            if mostrar_grafico == 1:
                self._grafico_gastos_setor()
            elif mostrar_grafico ==2:
                self._grafico_gastos_gerais()
            elif mostrar_grafico==3:
                self._grafico_lucro()
        else:
            print("Opção inválida! Prosseguindo...")
        self._formatar()

    def _grafico_gastos_gerais(self):
        erro=self._verificar_df()
        if erro:
            return print(erro)
        self.df['Vencimento']= pd.to_datetime(self.df['Vencimento'])
        gastos_pagos=self.df[self.df['Status']=='Pago']['Valor'].sum()
        gastos_pendentes=self.df[self.df["Status"]=='Pendente']['Valor'].sum()
        categories=['Pago','Pendente']
        values=[gastos_pagos,gastos_pendentes]
        plt.bar(categories, values, color=['green','red'])
        plt.title("Status das Contas - Janeiro 2026")
        plt.ylabel('Valor (R$)')
        plt.show()


    def _verificar_df(self):
        if self.df.empty:
            return f"Sem Dados dentro do arquivo {self.arquivo}"


    def _grafico_gastos_setor(self):
        erro=self._verificar_df()
        if erro:
            return print(erro)
        soma_por_categoria= self.df.groupby('Categoria')["Valor"].sum()
        plt.figure()
        soma_por_categoria.plot(kind="pie", autopct="%1.1f%%")
        plt.title("Gastos Por Setor")
        plt.ylabel('')
        plt.show()

    def _grafico_lucro(self):
        erro=self._verificar_df()
        if erro:
            return print(erro)
        soma_entrada=self.df[self.df['Tipo'] == 'Entrada']['Valor'].sum()
        soma_saida=self.df[self.df['Tipo'] == 'Saida']['Valor'].sum()
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

    def _formatar(self):
        wb = load_workbook(self.arquivo)
        ws = wb.active
        ws.column_dimensions['A'].width = 30
        ws.column_dimensions['B'].width = 15
        ws.column_dimensions['C'].width = 15
        ws.column_dimensions['D'].width = 20
        wb.save(self.arquivo)




sistema = ControleFinanceiro()
while True:
    continuar=int(input("[1] Para Adicionar\n"
    "[2] Para Mostrar Gráficos\n"
    "[3] Para Sair\n"
    "Escolha: "))
    if continuar == 1:
        sistema.adicionar_gasto()
    elif continuar == 2:
        sistema.gerar_graficos()
    elif continuar == 3:
        print('Saindo...')
        break
    else:
        print("Erro: Escolha inválida")

