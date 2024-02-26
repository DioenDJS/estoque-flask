<h1 align="center"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" width="65" alt="" />Estoque de e-commerce</h1>

<p align="center">
    <img src="https://img.shields.io/static/v1?label=DioenD&message=Python&color=d2cca1&labelColor=757780" alt="DioenD">
    <img src="https://img.shields.io/static/v1?label=NLW &message=Rocketseat&color=dfdfdf&labelColor=41356b" alt="hashtag">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/DioenDJS/estoque-flask" >
</p>

## Tecnologias Utilizadas no projeto :construction:

- [Flask](https://flask.palletsprojects.com/en/3.0.x/installation/) <img align="center" alt="scikit-learn" height="40" width="45" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/flask/flask-original.svg" style="max-width:100%;" />
- [Pillow](https://pillow.readthedocs.io/en/stable/index.html) 
- [Python-barcode](https://python-barcode.readthedocs.io/en/stable/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)
- [Cerberus](https://docs.python-cerberus.org/) <img align="center" alt="scikit-learn" height="40" width="30" src="https://docs.python-cerberus.org/_static/cerberus.png" />
- [Pytest](https://docs.pytest.org/en/8.0.x/) <img align="center" alt="scikit-learn" height="40" width="30" src="https://docs.pytest.org/en/8.0.x/_static/pytest_logo_curves.svg" />
## Projeto :computer:
![image](https://github.com/DioenDJS/estoque-flask/assets/76778401/e523f5c9-12e4-439a-a552-5b03165aba00)




    
## Como executar :gear:

- Clone o repositório `https://github.com/DioenDJS/estoque-flask.git`.
- remocer .config do arquivo `.env.config`
- Rode o projeto `docker-compose up` para iniciar a aplicação.
- Ao final a aplicação estará disponível em `http://localhost:3000`.

## Bibliotecas do Projetos :card_index_dividers:


- Flask
> ``` pip install Flask ```

- Pillow
> ``` pip install pillow ```

- Python-barcode
> ``` pip install python-barcode ```

- Cerberus
> ``` pip install Cerberus ```

- Pytest
>``` pip install pytest ```
> 
> comando para rodar os test
> 
> ```pytest -s -v```

### Criando arquivo .txt com as dependências: 
> ```venv/Scripts/pip3 freeze > requirements.txt```

## postman

### Tag

- Create
  
  ![Captura de tela 2024-02-12 180724](https://github.com/DioenDJS/estoque-flask/assets/76778401/d8bd83d0-7d58-4016-9738-d2e7ec3d0cd9)

- Tag(codigo de barra) generated
  
  ![Captura de tela 2024-02-12 181053](https://github.com/DioenDJS/estoque-flask/assets/76778401/35baf4d7-3ad9-418a-8a8b-f1fc9229c360)

### Product

- Create

![image](https://github.com/DioenDJS/estoque-flask/assets/76778401/f114ab30-f86d-405d-b96a-1398321ae14b)

 - Find All Product

 ![image](https://github.com/DioenDJS/estoque-flask/assets/76778401/fdb2353f-7127-4a2c-bb15-622f419f835c)


### User

- Create
![Captura de tela 2024-02-25 101807](https://github.com/DioenDJS/estoque-flask/assets/76778401/4a31e1ea-5469-47b3-a54c-9e25360dbd95)


### Auth

- Login
![Captura de tela 2024-02-25 101233](https://github.com/DioenDJS/estoque-flask/assets/76778401/9f9bfa22-8923-44b6-aa00-0bae34fd2080)


![image](https://github.com/DioenDJS/estoque-flask/assets/76778401/ea8bb34d-597b-42ce-9651-112611d7a149)
>script pra setar o token gerado em uma variavel de ambiente do Postman
```
// Extrai o access_token da resposta
var jsonData = JSON.parse(responseBody);
var accessToken = jsonData.access_token;

// Define o access_token como variável de ambiente
pm.environment.set("access_token", accessToken);
```

### Employee

- create
![Captura de tela 2024-02-26 122320](https://github.com/DioenDJS/estoque-flask/assets/76778401/6cea6161-cb9a-4594-b72c-57e5dea49907)

- list all
![Captura de tela 2024-02-26 122450](https://github.com/DioenDJS/estoque-flask/assets/76778401/98b2f526-2e6f-40e4-a6b6-57444e688638)

- list by id
![Captura de tela 2024-02-26 122609](https://github.com/DioenDJS/estoque-flask/assets/76778401/36c973b9-42dd-451b-b863-b62738d0b2b6)

- delete
![image](https://github.com/DioenDJS/estoque-flask/assets/76778401/90223628-7201-4d8f-84bb-32e211bf65f2)








  

