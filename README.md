# 💰 Sistema de Controle Financeiro via WhatsApp

Este projeto é um bot de gestão financeira que utiliza **Python**, **Flask** e a **API do Twilio** para permitir o registro e consulta de gastos diretamente pelo WhatsApp.

## 🚀 Funcionalidades
- **Registro de Gastos:** Salva valor, descrição e categoria em uma planilha Excel automaticamente.
- **Relatórios Visuais:** Gera gráficos de pizza (por categoria) e de barras (balanço mensal).
- **Busca Inteligente:** Localiza gastos específicos por termo.
- **Gestão de Dados:** Interface integrada com **Pandas** para manipulação de planilhas.

## 🛠️ Tecnologias Utilizadas
- Python 3.x
- Flask (Servidor Web)
- Twilio API (Integração WhatsApp)
- Pandas (Manipulação de dados)
- Matplotlib (Geração de gráficos)
- ngrok (Tunelamento local)

## 📦 Como Instalar e Rodar
1. Clone o repositório:
   ```bash
   git clone [https://github.com/KugikiBF/Python_Whatsapp_FinanceSystem]
Instale as dependências:

Bash
pip install -r requirements.txt
Inicie o servidor local:

Bash
python app.py
Em outro terminal, inicie o ngrok:

Bash
.\ngrok.exe http 5000
Configure a URL gerada pelo ngrok no console da Twilio adicionando /bot ao final.


---

Fazendo isso, o seu nível de profissionalismo vai lá no alto! Conseguiu gerar o `requirements.txt` aí? Se ele ficou muito gigante com coisas que você não usa, me avisa que te ensino a limpar!