import requests
from urllib.parse import urlencode

class PagSeguroAPI:
    def __init__(self, email, token, sandbox=True):
        self.email = email
        self.token = token
        self.base_url = "https://ws.sandbox.pagseguro.uol.com.br/v2" if sandbox else "https://ws.pagseguro.uol.com.br/v2"

    def criar_sessao(self):
        endpoint = f"{self.base_url}/sessions"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        params = {
            'email': self.email,
            'token': self.token,
        }

        response = requests.post(endpoint, headers=headers, params=params)
        return response.json()

    def criar_pedido(self, referencia, descricao, valor):
        endpoint = f"{self.base_url}/transactions"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        params = {
            'email': self.email,
            'token': self.token,
        }

        # Dados do pedido
        data = {
            'currency': 'BRL',
            'itemId1': '1',
            'itemDescription1': descricao,
            'itemAmount1': str(valor),
            'itemQuantity1': '1',
            'reference': referencia,
        }

        response = requests.post(endpoint, headers=headers, params=params, data=urlencode(data))
        return response.json()

if __name__ == "__main__":
    # Substitua 'SEU_EMAIL' e 'SEU_TOKEN' pelos seus dados reais
    pagseguro_api = PagSeguroAPI(email='SEU_EMAIL', token='SEU_TOKEN')

    # Criar uma sessão (necessário para iniciar a integração)
    sessao = pagseguro_api.criar_sessao()
    print("ID da Sessão:", sessao['id'])

    # Criar um pedido
    referencia_pedido = '12345'  # Substitua pela referência do seu pedido
    descricao_produto = 'Produto Teste'
    valor_produto = 10.00  # Substitua pelo valor do seu produto

    resposta_pedido = pagseguro_api.criar_pedido(referencia_pedido, descricao_produto, valor_produto)
    print("URL de pagamento:", resposta_pedido['paymentLink'])
