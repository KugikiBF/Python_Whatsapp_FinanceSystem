from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from index import ControleFinanceiro
from random import randint

app=Flask(__name__)
sistema=ControleFinanceiro()

estado_usuario={}

@app.route('/bot', methods=['POST'])
def bot():
    wpp_id=request.values.get("From")
    host = request.headers.get('Host')
    base_url = f"https://{host}/"
    mensagem_usuario= request.values.get("Body", '').strip()
    resp=MessagingResponse()
    msg=resp.message()
    mensagem_dividida=mensagem_usuario.split()

    if wpp_id in estado_usuario and estado_usuario[wpp_id] == 'MENU_GRAFICOS':
        if mensagem_usuario == '1':
            msg.body("*Balanço geral:*")
            sistema.grafico_lucro_wpp()
            msg.media(f'{base_url}static/lucro.png?v={randint(1,10000)}')
            del estado_usuario[wpp_id]

        elif mensagem_usuario =='2':
            msg.body("*Gráfico por categoria:*")
            sistema.grafico_setor_wpp()
            msg.media(f'{base_url}static/pizza.png?v={randint(1,10000)}')
            del estado_usuario[wpp_id]

        elif mensagem_usuario =='3':
            msg.body("*Gastos Pagos/Pendentes:*")
            sistema.grafico_gerais_wpp()
            msg.media(f'{base_url}static/gerais.png?v={randint(1,10000)}')
            del estado_usuario[wpp_id]
        elif mensagem_usuario =='4':
            msg.body(f"{sistema.historico_contas()}")
            del estado_usuario[wpp_id]
        else:
            msg.body("Opção inválida! Digite (*1 2 3 4*) para ver os gráficos")
      

    elif mensagem_usuario.lower() == 'excluir':
        msg.body(f"{sistema.excluir_lançamento()}")
       


    elif mensagem_usuario.lower().startswith("buscar:"):
        termo=mensagem_usuario.split(":")[1].strip()
        resposta=sistema.buscar_wpp(termo)
        msg.body(resposta)
        



    elif mensagem_usuario == '?':
            todas_saidas = ', '.join(sistema.categorias["Saidas"])
            todas_entradas = ', '.join(sistema.categorias["Entradas"])
            
            texto_ajuda = (
                "🤖 *GUIA DE FUNCIONALIDADES*\n\n"
                "📝 *Adicionar Gasto:* `Valor Descrição Categoria` \n"
                "_(Ex: 50 Uber Lazer)_\n\n"
                "📊 *Relatórios:* Digite `resumo` para ver gráficos e histórico.\n\n"
                "🔍 *Buscar:* `buscar: termo` \n"
                "_(Ex: buscar: mercado)_\n\n"
                "🗑️ *Apagar:* Digite `excluir` para remover o último lançamento.\n\n"
                "📌 *Categorias Disponíveis:*\n"
                f"🔺 *Saídas:* {todas_saidas}\n"
                f"🔹 *Entradas:* {todas_entradas}"
            )
            msg.body(texto_ajuda)


    elif mensagem_usuario.lower() == 'resumo':
        estado_usuario[wpp_id] = 'MENU_GRAFICOS'
        msg.body("📊 *Menu de Gráficos*\n\n1 - Balanço Geral (Barras)\n2 - Gastos por Categoria (Pizza)\n3 - Gastos pagos e pendentes (Barras)\n4 - Ver Histórico \n\nDigite o número desejado:")
        
        

    elif len(mensagem_dividida) >= 3:
        try:
            valor_limpo = mensagem_dividida[0].replace(',', '.')
            float(valor_limpo) # Validação técnica
            
            descricao = mensagem_dividida[1]
            categoria = mensagem_dividida[2].capitalize()
            todas_categ = sistema.categorias['Saidas'] + sistema.categorias['Entradas']
            
            if categoria in todas_categ:
                resultado = sistema.adicionar_pelo_wpp(valor_limpo, descricao, categoria)
                msg.body(resultado)
            else:
                msg.body(f"❌ Categoria '{categoria}' não existe.\nUse: {', '.join(todas_categ)}")
        except ValueError:
            msg.body("🤖 Formato incorreto. Para salvar use: `Valor Descricao Categoria`")
            

    else:
        msg.body("🤖 Olá! Não entendi seu comando.\n\nDigite `?` para ver tudo o que eu posso fazer!")
        
    
    
    response_xml = str(resp)
    print(f"DEBUG XML: {response_xml}") 
    return response_xml, 200, {'Content-Type': 'text/xml'}

if __name__ == '__main__':
    app.run(debug=True)