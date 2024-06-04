Projeto Controle de Estoque

- A aplicação apresenta à empresa DSofs, uma loja que possui diversas bebidas, um programa que controla o estoque da empresa, mostrando informações sobre as bebidas através de uma lista e o cadastro de um produto através de um formulário. Se o usuário for
  um administrador, ele ainda pode editar e excluir um produto através de botões que aparecem na lista. Se o usuário for um funcionário, ele só pode visualisar e cadastrar os produtos. Antes de tudo, o usuário precisa informar seu nome e senha, que somente
  são criados dentro do banco de dados. Caso o usuário escolha sair do sistema, ele terá que logar novamente, e não conseguirá acessar as rotas através da URL.

- OBS:
  - 1. Ao baixar os arquivos, atente-se que o arquivo db.sql possui os comandos que foram utilizados para criar o banco de dados. Apenas copie e cole no seu MySQL.
  - 2. No arquivo main.py, na linha 13 no comando app.config, atente-se em colocar as informações corretas do seu banco de dados.
  - 3. Utilize no terminal, os comandos:
    - pip install flask
    - pip install flask-sqlalchemy
    - pip install mysql-connector-python
  - 4. Os usuários com seus nomes e senhas que vem como padrão no comentário INSERT INTO do arquivo MySQL são:
    - Administradores:
      - Nome: Lucas, Senha: Lucas;
      - Nome: Shaihanne, Senha: Shaihanne;
    - Funcionários:
      - Nome: Pedro, Senha: Pedro;
      - Nome: Geovane, Senha: Geovane;
    - Caso queira adicionar um novo funcionário, a coluna 'isAdmin' precisa ser 0
    - Caso queira adicionar um novo administrador, a coluna 'isAdmin' precisa ser 1
