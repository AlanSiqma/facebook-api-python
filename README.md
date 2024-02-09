# Envio mensagens Facebook Python 🐍

## O que é ?
O envio de mensagens para uma pagina do Facebook usando Python é um processo de automatização no qual você pode programar um script em Python para enviar mensagens para paginas específicos no Facebook. 

## E esse bot o que faz? 
Responsavel por mandar mensagens para a pagina

## Pré-requisitos
Antes de começar, certifique-se de ter os seguintes itens instalados em seu sistema:

- Python 3.x
- Pip (gerenciador de pacotes do Python)
- Conta no Facebook
- Página do Facebook da qual você é administrador

## Configurações

### 1- Criar um Token no Facebook:

Obtenha um token de acesso para a API do Facebook. Você pode gerar um token de acesso na página de desenvolvedores do Facebook.


### 2- Instale o Python

[Clique aqui](https://www.python.org/downloads/), e você será redirecionado para a instalação do Python.

### 3- Baixe alguns pacotes

No CMD, digite os comandos:
```
pip install facebook
```
```
pip install python-dotenv
```

### 4- Crie as variaveis de ambientes

Na raiz do projeto crie um arquivo .env
nele você ira adicionar:
```
webhook = "o token que você pegou no passo 1"
```

#### Observações
Certifique-se de que a página para a qual você deseja enviar mensagens seja gerenciada pela mesma conta do Facebook que você utilizou para obter o token de acesso.

Este bot destina-se apenas a fins educacionais e de demonstração. O uso indevido deste bot pode violar os Termos de Serviço do Facebook.