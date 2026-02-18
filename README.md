# 🤖 WhatsApp Financial Bot (Twilio + Flask)

Este projeto é um assistente financeiro inteligente integrado ao WhatsApp que utiliza inteligência de dados para gerir gastos e entradas diretamente pelo chat. O sistema processa mensagens em tempo real, armazena informações em planilhas Excel e gera dashboards visuais de desempenho financeiro.

## 🚀 Funcionalidades

- **Lançamentos Rápidos:** Registro de transações via texto simples (Ex: `50 Almoço Lazer`).
- **Dashboard sob Demanda:** Geração de gráficos de pizza (gastos por setor) e barras (lucro vs. prejuízo) enviados diretamente no chat.
- **Busca Avançada:** Localização de itens no histórico através do comando `buscar:`.
- **Controle de Status:** Gestão de contas pagas e pendentes.
- **Persistência em Excel:** Motor de dados baseado em `.xlsx`, facilitando a portabilidade para usuários leigos.

## 🛠️ Tecnologias

- **Linguagem:** Python 3.x
- **Framework Web:** Flask (Webhooks)
- **Análise de Dados:** Pandas
- **Gráficos:** Matplotlib (Engine Agg para renderização em servidor)
- **Manipulação de Planilhas:** Openpyxl
- **API de Mensageria:** Twilio API for WhatsApp

## 📋 Comandos do Bot

- `?`: Exibe o guia de funcionalidades e categorias.
- `resumo`: Abre o menu interativo de gráficos.
- `buscar: termo`: Filtra lançamentos pela descrição.
- `excluir`: Remove o último lançamento realizado.
- `Valor Descrição Categoria`: Formato padrão para adicionar novos registros.

## 🔧 Configuração e Instalação

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/KugikiBF/Python_Whatsapp_FinanceSystem.git]
Instalar dependências:

Bash
pip install flask pandas matplotlib openpyxl twilio
Estrutura de Pastas:
Certifique-se de ter a pasta static/ criada na raiz para o armazenamento temporário dos gráficos gerados.

Execução:

Bash
python app.py
Nota de Desenvolvimento: O projeto encontra-se em transição de arquitetura (WhatsApp para Telegram) visando escalabilidade e redução de custos operacionais de API.
