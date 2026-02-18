# 🤖 WhatsApp Financial Bot (Twilio + Flask)

Sistema de gestão financeira operado via WhatsApp que automatiza o registro de despesas e receitas, gerando relatórios visuais instantâneos. O projeto utiliza Python para processar mensagens via Webhook e organiza os dados em Excel para facilitar o acesso do usuário final.

## 🚀 Funcionalidades Principais

- **Registro via Linguagem Natural:** Adicione gastos enviando apenas `Valor Descrição Categoria` (Ex: `25.50 Almoço Fixo`).
- **Dashboard no Chat:** Geração automática de gráficos de pizza e barras para análise de saúde financeira.
- **Busca por Termos:** Filtro inteligente de lançamentos anteriores através do comando `buscar:`.
- **Persistência de Dados:** Banco de dados baseado em Excel (`.xlsx`) com formatação automática de colunas via `openpyxl`.
- **Menu Interativo:** Sistema de estados para navegação em menus de relatórios e histórico.

## 🛠️ Stack Técnica

- **Backend:** Python / Flask
- **Processamento de Dados:** Pandas
- **Visualização:** Matplotlib (Backend Agg)
- **Mensageria:** Twilio API (WhatsApp Business)
- **Planilhas:** Openpyxl

## 📋 Comandos Disponíveis

| Comando | Ação |
| :--- | :--- |
| `?` | Exibe o guia completo de categorias e uso. |
| `resumo` | Abre o menu de gráficos (Balanço, Setores, Status). |
| `buscar: termo` | Pesquisa transações por descrição. |
| `excluir` | Remove o último lançamento realizado. |
| `Valor Desc Categ` | Salva uma nova transação. |

## 🔧 Como Rodar o Projeto

1. Instale as dependências:
   ```bash
   pip install flask pandas matplotlib openpyxl twilio
Certifique-se de que a pasta static/ existe no diretório raiz (onde os gráficos serão gerados).

Inicie o servidor:

Bash
python app.py
Configure o Webhook da sua Sandbox Twilio para o endereço do seu servidor (ou túnel via Ngrok).

Desenvolvido por Bruno Felipe Mafra Lacerda LinkedIn | GitHub

