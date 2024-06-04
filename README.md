Projeto Controle de Estoque

A aplicação apresentada à empresa DSofs, uma loja especializada na venda de diversas bebidas, consiste em um programa de controle de estoque que exibe informações detalhadas sobre os produtos por meio de uma lista e permite o cadastro de novas bebidas por intermédio de um formulário. Ao iniciar a aplicação, é exibida uma tela de login que requer o nome de usuário e a senha. Caso o usuário seja um administrador, ele terá permissão não apenas para visualizar e cadastrar novas bebidas, mas também para editar e excluir produtos, através de botões disponíveis na lista. Se o usuário for um funcionário, ele poderá apenas visualizar e cadastrar novos produtos.
  
Para gerenciar os usuários registrados no sistema ou adicionar novos usuários, é necessário acessar diretamente o banco de dados, onde os nomes de usuário e senhas são exclusivamente criados. Após efetuar o login, o usuário será redirecionado para a lista de bebidas cadastradas no sistema, a qual exibe informações como tipo, marca, fornecedor, preço de compra (por unidade), preço de venda (por unidade), data de entrada, data de validade e quantidade em estoque.

Acima da lista, há três botões: "Lista", que redireciona para a lista de bebidas; "Cadastrar", que leva ao formulário de cadastro; e "Sair", que realiza o logout e limpa a sessão do usuário. Ao optar por sair do sistema, o usuário terá que realizar o login novamente para acessar qualquer funcionalidade, não sendo possível acessar as rotas diretamente pela URL.

Caso um usuário tente acessar uma URL de administrador enquanto logado como funcionário, ou vice-versa, o programa redirecionará automaticamente para a página de login. Dessa forma, garante-se que apenas usuários com as permissões adequadas possam acessar as respectivas funcionalidades.

- OBS:
  - 1. Se atente que os arquivos HTML estão dentro da pasta "templates". Não se esqueça de criá-la e colocar os arquivos dentro dela.
  - 2. Ao baixar os arquivos, atente-se que o arquivo "db.sql" possui os comandos que foram utilizados para criar o banco de dados. Apenas copie e cole no seu MySQL.
  - 3. No arquivo "main.py", na linha 13 no comando app.config, atente-se em colocar as informações corretas do seu banco de dados.
  - 4. No diretório raiz do projeto, utilize no terminal os comandos:
    - pip install flask;
    - pip install flask-sqlalchemy;
    - pip install mysql-connector-python.
  - 5. Os usuários com seus nomes e senhas que vem como padrão no comentário INSERT INTO do arquivo MySQL são:
    - Administradores:
      - Nome: Daniel, Senha: Daniel;
      - Nome: Lucas, Senha: Lucas;
      - Nome: Shaihanne, Senha: Shaihanne;
    - Funcionários:
      - Nome: Pedro, Senha: Pedro;
      - Nome: Geovane, Senha: Geovane.
    - Caso queira adicionar um novo funcionário, a coluna 'isAdmin' precisa ser 0
    - Caso queira adicionar um novo administrador, a coluna 'isAdmin' precisa ser 1

  - Metodologias utilizadas: Scrum, Kanban
  - Ferramentas utilizadas: VSCode, Python, Flask, MySQL, SQLAlchemy, mysql-connector-python, Bootstrap, HTML
 
  - Nome dos desenvolvedores que fizeram parte do projeto:
    - Pedro Henrique Vicino: Líder, Programação em Python, parte do Design
    - Shaihanne Allanis de Souza Oliveira: Banco de Dados
    - Lucas Lima Teles Silva: Restrição de Acesso
    - Geovane Geovane Bezerra dos Santos: Design, parte da Programação em Python
