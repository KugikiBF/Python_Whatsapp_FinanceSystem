# 🤖 WhatsApp Financial Bot | Python & Flask

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Twilio](https://img.shields.io/badge/Twilio-F22F46?style=flat&logo=Twilio&logoColor=white)](https://www.twilio.com/)

> **Status do Projeto:** Pausado (Migrando para Telegram devido a limitações de cota da API Twilio). Este repositório preserva a arquitetura funcional integrada ao WhatsApp.

## 📝 Sobre o Projeto
Este é um bot de controle financeiro inteligente operado inteiramente via WhatsApp. O objetivo foi criar uma ferramenta de alta acessibilidade para usuários que desejam gerir finanças pessoais sem a complexidade de aplicativos bancários ou planilhas manuais difíceis de operar no celular.

A lógica de negócio utiliza **Excel como motor de banco de dados**, permitindo que o usuário final tenha controle total e visual sobre os dados gerados pelo bot de forma simples e familiar.

## ✨ Funcionalidades Principais

-   **Registro Rápido via Chat:** Adicione gastos ou ganhos enviando apenas: `Valor Descrição Categoria` (Ex: `50 Uber Lazer`).
-   **Dashboard Visual Dinâmico:** Geração automática de gráficos:
    -   📊 Balanço Mensal (Lucro vs. Prejuízo).
    -   🍕 Distribuição de Gastos por Categoria (Gráfico de Pizza).
    -   📉 Status de Pagamentos (Pagos vs. Pendentes).
-   **Busca Inteligente:** Comando `buscar: termo` para encontrar lançamentos específicos rapidamente.
-   **Gestão de Estado:** Sistema de menu interativo que entende o contexto das mensagens do usuário.
-   **Exportação Transparente:** Todos os dados são salvos em um `.xlsx` formatado automaticamente via código.

## 🛠️ Tecnologias Utilizadas

-   **Backend:** Python com Microframework Flask.
-   **Data Science:** Pandas para manipulação de dados e análise financeira.
-   **Visualização:** Matplotlib para geração de gráficos salvos em buffer para envio via API.
-   **Integração de Mensageria:** Twilio API for WhatsApp (TwiML).

## 🚀 Como Executar (Local)

1. Clone o repositório:
   ```bash
   git clone [https://github.com/KugikiBF/Python_Whatsapp_FinanceSystem]

Instale as dependências:

    ```bash
        pip install flask pandas matplotlib openpyxl twilio
        Configure o Webhook no Twilio para utilizar o Ngrok para túnel local:

    ```bash
        python app.py
    
🧠 Insights do Desenvolvedor
A escolha do Excel em vez de um banco SQL tradicional foi uma decisão estratégica de Product Management: o usuário comum sente-se dono do dado quando pode abrir uma planilha. O desafio técnico foi garantir a integridade dos dados e a formatação automática das colunas via openpyxl a cada inserção.

Desenvolvido por Bruno Felipe Mafra Lacerda 📫 LinkedIn | GitHub

