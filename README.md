# ds-currency

# Desafio Técnico desenvolvedor backend Python/Django

Olá!

Esta é a API desenvovida como requisito de avaliação para a posição de desenvolvedor backend para a Data Stone. Possui como objetivo a cotação de valores em diferentes moedas.

## Características

- Desenvolvida em Django, linguagem Python.
- Estrutura baseada em Módulos, Models e Views.
- Previsão de consumo em Frontend usando requisições HTTP
- Espera como entradas: moeda de entrada, moeda de saída e valor a ser cotado
- Utiliza dados obtidos *on-demand* de API externa (https://www.abstractapi.com/), de modo a garantir que as cotações sejam atuais e fidedignas
- Possui como moeda de lastro USD (Dólar americano)
- Converte nativamente entre USD (Dólar amerciando), BRL (Real brasileiro), EUR (Euro), BTC (Bitcoin) e  ETH (Ethereum). 
- Possui testes unitários para funcionalidades específicas e estrutura para expansão das mesmas

## Requisitos:

A aplicação, como mencionado foi criada em Django, uma framework Python. Desta forma, a instalação de Python é requisito fundamental. O detalhamento abaixo inclui os requisitos mínimos para executar o projeto:

Obrigatórios:

- Python (foi utilizada a versão 3.10 para o desenvolvimento)
- Django
- Conexão com a internet (para aquisição dos dados de cotação e instalação de bibliotecas auxiliares)

Opcionais:

- Docker (para executar o container, mais detalhes abaixo)

## Como executar a aplicação

Foram pensadas duas possibilidades: Docker e instalação usual. Para ambos, deve-se inicialmente clonar o repositório (https://github.com/dandenardi/ds-currency). Isto resultará em uma pasta contendo a pasta do projeto (currency_data_stone), um Dockerfile, este README.md e requirements.txt. A seguir, estão descritos os dois modos para executar o projeto.

### Docker

Pré-requisitos:
- Docker instalado no sistema

Para utilizar a versão Docker, deve-se executar os seguintes comandos de dentro da pasta raiz (data-stone):
- docker build -t currency-data-stone .
- docker run -p 8000:8000 currency-data-stone

O primeiro comando criará o container do projeto e o segundo executará o container.

A partir daqui, é possível acessar o endereço localhost:8000. Caso veja uma página de boas-vindas, a geração do container foi bem sucedida.

### Instalação usual

Pré-requisitos:
- Nenhum

Para utilizar a versão direta a partir do repositório, após a clonagem descrita acima, deve-se:
- navegar para a sub-pasta do projeto (cd currency_data_stone)
- Inserir o comando pip install requirements.txt -r
- python manage.py runserver

A partir daqui, é possível acessar o endereço 127.0.0.1:8000 ou localhost:8000. Caso veja a página de boas-vindas, o projeto foi instalado e está pronto para ser utilizado.

## Fazer uma requisição à API

No momento, a API tem uma única endpoint pública que aceita requisições GET. A endpoint é a seguinte:

http://127.0.0.1:8000/api/currency-conversion/

Caso acessada desta forma (sem parâmetros adicionais), retornará a conversão entre dólar americano (USD) e real brasileiro (BRL) para o valor de 1.
Para alterar o tipo da moeda de entrada, deve-se incluir o parâmetro 'from', como no exemplo:

http://127.0.0.1:8000/api/currency-conversion?from=BRL

Já para incluir uma moeda de saída, deve-se incluir o parâmetro 'to':

http://127.0.0.1:8000/api/currency-conversion?to=EUR

E o valor a ser calculado/convertido é definido pelo parâmetro 'amount':

http://127.0.0.1:8000/api/currency-conversion?amount=20.3

Finalmente, uma versão completa de requisição seria algo na seguinte estrutura:

http://127.0.0.1:8000/api/currency-conversion/?from=BTC&to=BRL&amount=20.3

Ambos 'from' e 'to' são códigos de 3 dígitos que seguem a ISO 4217. Já amount deve ser um número do tipo float, com '.' para representar a separação decimal.

O retorno obtido será um JSON com a seguinte estrutura:

{
    "from_currency": <código de moeda de entrada>,
    "to_currency": <código de moeda de saída>,
    "exchange_rate": <taxa de câmbio obtida>,
    "amount": <valor inserido>,
    "converted_amount": <valor convertido>
}

## Fragilidades conhecidas

O sistema possui algumas fragilidades conhecidas:
- Não existe checagem no backend de tipos de dados. Uma requisição com dados fora dos especificados acima, resultará em erro.
- As solicitações para a API demandam uma chave de usuário única. Esta chave está incluída no corpo do código, o que não é recomendado. No entanto, considerou-se o caso atual
como teste do tipo Prova Conceito (POC). Em uma versão definitiva, esta informação estaria contida em setor separado como ENV, local com criptografia ou, ainda melhor, a geração de uma chave para cada usuário. No entanto, foi suposto que algo assim não seria ideal nesta etapa, tendo em vista que a API utilizada possivelmente seria substituída em uma aplicação
em produção.
- Ainda relacionado à API, a solução encontrada não é a mais robusta do mercado, servindo para os propósitos de teste. Uma alternativa não foi buscada de forma exaustiva.
- O servidor em Django prevê uma estrutura escalável com banco de dados. No momento, optou-se por apenas retornar os valores solicitados, sem persistência. Porém, existe a
possibilidade de adição destas funcionalidades num futuro.
- O painel de administração possui um superusuário chamado admin. Este usuário possui uma senha padrão sem complexidade. Em um ambiente de produção, este usuário precisaria ser
recriado com maior atenção para aspectos de segurança.
 
## Escolhas técnicas

São descritas aqui as razões norteadoras para a adoação das tecnologias utilizadas:
- Django foi utilizada para a criação da API considerando os critérios para a vaga.
- Docker foi adotado por ter sido mencionado como ideal para execução do projeto. Não foi descartada, no entanto, a adoção de uma execução mais comumente utilizada.
- O uso de uma API externa para obtenção das taxas de conversão foi considerado de modo a cobrir o requisito de dados atuais e reais.
- O retorno em JSON também é requisito do projeto
- A estrutura geral do projeto foi adotada de modo a condizer com os requisitos e seguir o padrão do framework, auxiliando na manutenção e legibilidade

## Concluindo

Este é um resumo das funcionalidades contidas na API. Tem como objetivo uma conversão simples entre moedas. Sendo uma API, pode ser utilizada para prover dados para
diversos outros sistemas, como aplicações web ou aplicações móveis. Para mais informações, fica à disposição o e-mail do autor: dan.denardi@gmail.com. 

Agradeço a disponibilidade até aqui e oportunidade para demonstrar estas funcionalidades!

Forte abraço!