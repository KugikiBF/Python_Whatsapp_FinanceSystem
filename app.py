from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from index import ControleFinanceiro


app=Flask(__name__)
sistema=ControleFinanceiro()

@app.route('/bot', methods=['POST'])
def bot():
    mensagem_usuario= request.values.get("Body", '').strip()

    resp=MessagingResponse()
    msg=resp.message()
    mensagem_dividida=mensagem_usuario.split()
    if len(mensagem_dividida)>=3:
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
        msg.body("🤖 Comandos:\nPara salvar: *Valor Descricao Categoria*\nEx: 50 Pizza Lazer")
    
    
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)