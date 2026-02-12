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
            # msg.media(f'{base_url}static/lucro.png?v={randint(1,10000)}')
            del estado_usuario[wpp_id]

        elif mensagem_usuario =='2':
            msg.body("*Gráfico por categoria:*")
            sistema.grafico_setor_wpp()
            # msg.media(f'{base_url}static/pizza.png?v={randint(1,10000)}')
            del estado_usuario[wpp_id]

        elif mensagem_usuario =='3':
            msg.body("*Gastos Pagos/Pendentes:*")
            sistema.grafico_gerais_wpp()
            # msg.media(f'{base_url}static/gerais.png?v={randint(1,10000)}')
            del estado_usuario[wpp_id]
        elif mensagem_usuario =='4':
            msg.body('Saindo Do Menu...')
            del estado_usuario[wpp_id]
        else:
            msg.body("Opção inválida! Digite (*1 2 3*) para ver os gráficos ou *4* para sair.")
        return str(resp)



    elif mensagem_usuario == '?':
        msg.body(f"Para adicionar um gasto é necessário seguir um padrão que seria:\n    (*Valor* *Descrição* *Categoria*)\n\nAs categorias são divididas em 2, uma para saidas, e outra para entradas.\n\n*Saídas:*\n    {', '.join(sistema.categorias["Saidas"])}.\n*Entradas:*\n    {', '.join(sistema.categorias["Entradas"])}.")


    elif mensagem_usuario.lower() == 'resumo':
        estado_usuario[wpp_id] = 'MENU_GRAFICOS'
        msg.body("📊 *Menu de Gráficos*\n\n1 - Balanço Geral (Barras)\n2 - Gastos por Categoria (Pizza)\n3 - Gastos pagos e pendentes (Barras)\n4 - SAIR \n\nDigite o número desejado:")
        return str(resp)
        

    elif len(mensagem_dividida)>=3:
        try:
            valor= mensagem_dividida[0].replace(',','.')
            descricao=mensagem_dividida[1]
            categoria=mensagem_dividida[2].capitalize()

            todas_categ=sistema.categorias['Saidas'] + sistema.categorias['Entradas']
            
            if categoria in todas_categ:
                resultado = sistema.adicionar_pelo_wpp(valor, descricao, categoria)
                msg.body(resultado)
            else:
                msg.body(f"❌ Categoria '{categoria}' não existe.\nUse: {', '.join(todas_categ)}")
        except ValueError:
            msg.body("❌ Erro no valor! Use: 'Valor' 'Descricao' 'Categoria' (Ex: 50 Uber Lazer)")


    else:
        msg.body("🤖 Comandos:\nPara salvar: *Valor Descricao Categoria*\nEx: 50 Pizza Lazer\n"
                 "Para dúvidas: Digite ('?')")
    
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True, port=5001)