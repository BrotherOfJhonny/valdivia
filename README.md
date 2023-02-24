# valdivia

![valdivia](/img/imagem1.jpg)

## Introdução

Este script em Python permite testar se um determinado site está executando um servidor XML-RPC e verificar quais métodos estão disponíveis para chamada. O script também inclui testes de pingback e login, permitindo que você verifique se o servidor está configurado corretamente.
É possível realizar os seguintes testes:

- Teste sayHello: testa a comunicação XML-RPC básica.
- Teste pingback: testa a funcionalidade de pingback em um site.
- Teste de métodos ativos: lista os métodos XML-RPC disponíveis em um site.
- Teste de login: testa a autenticação XML-RPC em um site.

## Pré-requisitos

Antes de usar o script, certifique-se de ter o Python 3 instalado no seu sistema. Você também precisará instalar a biblioteca xmlrpc.client para fazer as chamadas XML-RPC. Para instalar a biblioteca, você pode executar o seguinte comando:

```python
pip install -r requirements.txt
```

## Como usar
Clone o repositório ou faça o download do arquivo valdivia.py
Abra um terminal na pasta onde o arquivo valdivia.py está localizado.
Execute o comando abaixo para executar o script:

```python
python valdivia.py
```

Insira as informações solicitadas pelo script, seguindo as instruções apresentadas na tela.
Resultados

### Testes

**Teste sayHello**
O primeiro teste que o script executará é o sayHello, que chama o método demo.sayHello() no servidor XML-RPC. Este é um método de teste simples que retorna uma mensagem de boas-vindas.

Se o teste sayHello for executado com sucesso, você verá uma mensagem em verde indicando que o teste foi bem-sucedido. Caso contrário, você verá uma mensagem em vermelho indicando que ocorreu um erro.

![hello](/img/sayhello.jpg)


**Teste pingback**

O próximo teste que o script executará é o pingback. O teste de pingback verifica se o servidor está configurado corretamente para aceitar chamadas de pingback de outros sites.

Para executar o teste de pingback, você precisará inserir o endereço completo do site que deseja testar.

Se o teste de pingback for executado com sucesso, você verá uma mensagem em verde indicando que o teste foi bem-sucedido e a resposta do servidor será exibida em azul. Caso contrário, você verá uma mensagem em vermelho indicando que ocorreu um erro.

![pingback](/img/pingback.jpg)



**Teste de métodos ativos**

Este teste lista os métodos XML-RPC disponíveis em um site. Você precisará fornecer o endereço do sistema que deseja testar. Se o teste for bem-sucedido, uma lista de métodos disponíveis será exibida em laranja.

![métodos](/img/metodos.jpg)


**Teste de login**

O último teste que o script executará é o teste de login. O teste de login tentará fazer login no servidor XML-RPC com um nome de usuário e senha fornecidos. O script solicitará que você insira o nome de usuário que deseja testar e, em seguida, o caminho para um arquivo contendo senhas que você deseja testar.

Se o teste de login for bem-sucedido, você verá uma mensagem em verde indicando que o login foi bem-sucedido e o nome de usuário e senha que foram usados para fazer login serão exibidos. Caso contrário, você verá uma mensagem em vermelho indicando que ocorreu um erro.

![login](/img/login.jpg)


#### Observação

Este script é útil para verificar rapidamente se um site está executando um servidor XML-RPC e quais métodos estão disponíveis para chamada. Com isso, você pode encontrar possíveis vulnerabilidades em sistemas que possuem a funcionalidade XML

O script foi desenvolvido com auxilio do ChatGPT, com fins educacionais e não deve ser utilizado para testes de invasão não autorizados ou para violar a privacidade de outras pessoas. O autor deste script não se responsabiliza pelo uso indevido do mesmo.
