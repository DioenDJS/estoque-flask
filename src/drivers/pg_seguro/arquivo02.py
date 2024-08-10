import requests

class PagSeguroAPI:
    def __init__(self, email, token):
        self.email = email
        self.token = token
        self.base_url = "https://ws.sandbox.pagseguro.uol.com.br/v2"  # Use o ambiente de sandbox para testes

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

    # Adicione mais métodos conforme necessário para interagir com outros recursos da API do PagSeguro

if __name__ == "__main__":
    # Substitua 'SEU_EMAIL' e 'SEU_TOKEN' pelos seus dados reais
    pagseguro_api = PagSeguroAPI(email='SEU_EMAIL', token='SEU_TOKEN')

    # Criar uma sessão (necessário para iniciar a integração)
    sessao = pagseguro_api.criar_sessao()
    print("ID da Sessão:", sessao['id'])
