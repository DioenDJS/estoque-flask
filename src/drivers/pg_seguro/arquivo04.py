from flask import Flask, request

app = Flask(__name__)

@app.route('/notificacao_pagseguro', methods=['POST'])
def notificacao_pagseguro():
    try:
        # Receber os dados da notificação
        dados_notificacao = request.form.to_dict()

        # Verificar a autenticidade da notificação (opcional, mas altamente recomendado)
        # Certifique-se de verificar se o IP de origem está na lista de IPs do PagSeguro
        # e valide a autenticidade usando as credenciais (token)
        # ...

        # Processar os dados da notificação
        status_transacao = dados_notificacao.get('status', '')
        referencia = dados_notificacao.get('reference', '')

        # Adicione lógica adicional para processar o status da transação e atualizar seu sistema
        # ...

        return 'OK', 200  # Responde ao PagSeguro indicando que a notificação foi recebida com sucesso
    except Exception as e:
        print(f"Erro ao processar notificação: {str(e)}")
        return 'Erro', 500  # Responda com um erro para que o PagSeguro tente novamente

if __name__ == '__main__':
    app.run(debug=True, port=5000)
