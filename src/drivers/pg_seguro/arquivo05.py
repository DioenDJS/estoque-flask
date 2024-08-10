from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

# Substitua 'SEU_EMAIL' e 'SEU_TOKEN' pelos seus dados reais
email_pagseguro = 'SEU_EMAIL'
token_pagseguro = 'SEU_TOKEN'


@app.route('/criar_pedido/<referencia>/<descricao>/<valor>', methods=['GET'])
def criar_pedido(referencia, descricao, valor):
    # Crie a URL de pagamento
    url_pagamento = gerar_url_pagamento(referencia, descricao, valor)

    # Redirecione o usuário para a página de pagamento do PagSeguro
    return redirect(url_pagamento)


def gerar_url_pagamento(referencia, descricao, valor):
    base_url_pagseguro = 'https://pagseguro.uol.com.br/checkout/v2'
    sandbox_url_pagseguro = 'https://sandbox.pagseguro.uol.com.br/checkout/v2'

    url_pagseguro = sandbox_url_pagseguro  # Use o ambiente de sandbox para testes

    url_pagseguro += '/checkout.html?'
    url_pagseguro += f'email={email_pagseguro}&token={token_pagseguro}'
    url_pagseguro += f'&currency=BRL&reference={referencia}&itemDescription1={descricao}'
    url_pagseguro += f'&itemAmount1={valor}&itemQuantity1=1'

    return url_pagseguro


if __name__ == '__main__':
    app.run(debug=True)
