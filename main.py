# Importação de bibliotecas necessárias do Flask
from flask import Flask, render_template, request, redirect, jsonify, send_from_directory, render_template_string, session
from flask_sqlalchemy import SQLAlchemy
import os

# Criação de uma instância do Flask
app = Flask(__name__)

# Chave secreta para sessions do Flask
app.secret_key = 'usuario_logado'

# Configuração do banco de dados usando SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='cida2011',
        servidor='localhost',
        database='controle_de_estoque'
    )

# Inicialização do objeto SQLAlchemy
db = SQLAlchemy(app)

# Definição de modelos de dados usando SQLAlchemy ORM
class estoque(db.Model):
    # Modelo para a tabela "Estoque"
    id_estoque = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome_produto = db.Column(db.String(50), nullable=False)
    marca = db.Column(db.String(50), nullable=False)
    fornecedor = db.Column(db.String(50), nullable=False)
    data_valid = db.Column(db.Date, nullable=False)
    data_de_entrada = db.Column(db.Date, nullable=False)
    preco_compra = db.Column(db.Float, nullable=False)
    qtd_em_estoque = db.Column(db.Integer, nullable=False)
    fk_estoq_plo = db.Column(db.Integer, nullable=True)

class plo(db.Model):
    # Modelo para a tabela "Plo"
    id_plo = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome_prod_plo = db.Column(db.String(50), nullable=False)
    marca_plo = db.Column(db.String(50), nullable=False)
    forn_plo = db.Column(db.String(50), nullable=False)
    data_entrada_plo = db.Column(db.Date, nullable=False)
    qtd_estoq_plo = db.Column(db.String(50), nullable=False)
    entrada_prod_plo = db.Column(db.String(50), nullable=False)
    saida_prod_plo = db.Column(db.String(50), nullable=False)
    status_disp_plo = db.Column(db.String(50), nullable=False)
    fk_usuario = db.Column(db.Integer, nullable=True)

class produtos(db.Model):
    # Modelo para a tabela "Produtos"
    id_produtos = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_produtos = db.Column(db.String(50), nullable=False)
    marca = db.Column(db.String(50), nullable=False)
    forn_prod = db.Column(db.String(50), nullable=False)
    data_valid_prod = db.Column(db.Date, nullable=False)
    data_entrada_prod = db.Column(db.Date, nullable=False)
    preco_compra = db.Column(db.Float, nullable=False)
    preco_venda = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    fk_estoque = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return '<Name %r>' % self.name

class usuario(db.Model):
    # Modelo para a tabela "Usuario"
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    senha_hash = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    telefone = db.Column(db.Integer, nullable=False)
    isAdmin = db.Column(db.Boolean, nullable=False)

# Rotas e funções do Flask
@app.route('/listaAdmin')
def listaAdmin():
    if 'admin_logado' not in session or session['admin_logado'] == None :
	    return redirect('/')
    # Rota para exibir uma lista de produtos
    lista_produtos = produtos.query.order_by(produtos.id_produtos)
    session.pop('funcionario_logado', None)
    return render_template("lista_admin.html", todos_produtos=lista_produtos)

@app.route('/listaFuncionario')
def listaFuncionario():
    if 'funcionario_logado' not in session or session['funcionario_logado'] == None :
	    return redirect('/')
    # Rota para exibir uma lista de produtos
    lista_produtos = produtos.query.order_by(produtos.id_produtos)
    session.pop('admin_logado', None)
    return render_template("lista_funcionario.html", todos_produtos=lista_produtos)

@app.route('/cadastroAdmin')
def cadastrarAdmin():
    if 'admin_logado' not in session or session['admin_logado'] == None:
	    return redirect('/')
    # Rota para exibir o formulário de cadastro
    return render_template('cadastro_admin.html')

@app.route('/cadastroFuncionario')   
def cadastrarFuncionario():
    if 'funcionario_logado' not in session or session['funcionario_logado'] == None:
	    return redirect('/')
    # Rota para exibir o formulário de cadastro
    return render_template('cadastro_funcionario.html')

@app.route('/adicionaAdmin', methods=['POST'])
def adicionaAdmin():
    # Rota para processar o formulário de cadastro e adicionar um novo produto ao banco de dados
    lista_produtos = produtos.query.order_by(produtos.id_produtos)
    
    # Obtendo os dados do formulário
    nome = request.form['txtNome']
    marca = request.form['txtMarca']
    quantidade = request.form['numQuantidade']
    forn_prod = request.form['txtFornecedor']
    preco_compra = request.form['txtPreçoCompra'].replace(',', '.')
    preco_compra = float(preco_compra) # Convertendo para float
    preco_venda = request.form['txtPreçoVenda'].replace(',', '.')
    preco_venda = float(preco_venda) # Convertendo para float
    data_entrada_prod = request.form['dateDataEntrada']
    data_valid_prod = request.form['dateDataValidade']
    
    # Criando uma nova instância do modelo de produto com os dados do formulário
    novo_produto = produtos(nome_produtos=nome,
                            marca=marca,
                            quantidade=quantidade,
                            forn_prod=forn_prod,
                            preco_compra=preco_compra,
                            preco_venda=preco_venda,
                            data_entrada_prod=data_entrada_prod,
                            data_valid_prod=data_valid_prod)

    # Adicionando o novo produto ao banco de dados
    db.session.add(novo_produto)

    # Salvando as mudanças no banco de dados
    db.session.commit()  

    # Redirecionando para a página de lista após a adição do produto
    return redirect('/listaAdmin')

@app.route('/adicionaFuncionario', methods=['POST'])
def adicionaFuncionario():
    # Rota para processar o formulário de cadastro e adicionar um novo produto ao banco de dados
    lista_produtos = produtos.query.order_by(produtos.id_produtos)
    
    # Obtendo os dados do formulário
    nome = request.form['txtNome']
    marca = request.form['txtMarca']
    quantidade = request.form['numQuantidade']
    forn_prod = request.form['txtFornecedor']
    preco_compra = request.form['txtPreçoCompra'].replace(',', '.')
    preco_compra = float(preco_compra) # Convertendo para float
    preco_venda = request.form['txtPreçoVenda'].replace(',', '.')
    preco_venda = float(preco_venda) # Convertendo para float
    data_entrada_prod = request.form['dateDataEntrada']
    data_valid_prod = request.form['dateDataValidade']
    
    # Criando uma nova instância do modelo de produto com os dados do formulário
    novo_produto = produtos(nome_produtos=nome,
                            marca=marca,
                            quantidade=quantidade,
                            forn_prod=forn_prod,
                            preco_compra=preco_compra,
                            preco_venda=preco_venda,
                            data_entrada_prod=data_entrada_prod,
                            data_valid_prod=data_valid_prod)

    # Adicionando o novo produto ao banco de dados
    db.session.add(novo_produto)

    # Salvando as mudanças no banco de dados
    db.session.commit()  

    # Redirecionando para a página de lista após a adição do produto
    return redirect('/listaFuncionario')

@app.route('/editar/<int:id>')
def editar(id) :
    # Rota para exibir o formulário de edição de um produto específico
    produtoSelecionado = produtos.query.filter_by(id_produtos = id).first()
    
    return render_template('editar.html', produto = produtoSelecionado)

@app.route('/atualizar', methods=['POST'])
def atualizar() :
    # Rota para processar a atualização dos dados de um produto específico
    produto = produtos.query.filter_by(id_produtos = request.form['txtID']).first()

    # As colunas da tabela Produtos recebem os dados do formulário
    produto.nome_produtos = request.form['txtNome']
    produto.marca = request.form['txtMarca']
    produto.quantidade = request.form['numQuantidade']
    produto.forn_prod = request.form['txtFornecedor']
    produto.preco_compra = float(request.form['txtPreçoCompra'].replace(',', '.'))
    produto.preco_venda = float(request.form['txtPreçoVenda'].replace(',', '.'))
    produto.data_entrada_prod = request.form['dateDataEntrada']
    produto.data_valid_prod = request.form['dateDataValidade']

    # Adicionando o novo produto ao banco de dados
    db.session.add(produto)
    
    # Salvando as mudanças no banco de dados
    db.session.commit()  

    # Ao atualizar o produto, o usuário é redirecionado à página de lista
    return redirect('/listaAdmin')

@app.route('/excluir/<int:id>')
def excluir(id):
    # Executa uma consulta para encontrar todos os registros na tabela 'Produtos'. Em seguida, deleta esses registros.
    produtos.query.filter_by(id_produtos = id).delete()

    # Confirma a transação no banco de dados, aplicando a exclusão realizada na linha anterior.
    db.session.commit()

    # Redireciona à rota /lista
    return redirect('/listaAdmin')

@app.route('/')
def index():
    # renderiza o arquivo login.html na rota principal
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():

    # Dados do formulário do login.html
    nome = request.form['txtNomeUsuario']
    senha_hash = request.form['txtSenha_hash']

    # Consulta o banco de dados para encontrar o usuário com o nome fornecido
    usuarios = usuario.query.filter_by(nome=nome).first()

    # Verifica se o usuário existe e se a senha fornecida corresponde à senha armazenada
    if usuarios and usuarios.senha_hash == senha_hash :
        if usuarios.isAdmin == 1:
        # Se as credenciais estiverem corretas, redireciona para a página /listaAdmin, lista do administrador
            session['admin_logado'] = nome
            return redirect('/listaAdmin')
        # Se as credenciais estiverem corretas, redireciona para a página /listaFuncionario, lista do funcionário
        elif usuarios.isAdmin == 0:
            session['funcionario_logado'] = nome
            return redirect('/listaFuncionario')
    else:
        # Se as credenciais estiverem incorretas, retorna uma mensagem de erro e um status HTTP 401 (não autorizado)
        return redirect('/')
@app.route('/logout')
def logout():
    # Limpa a sessão do usuário
    session.pop('admin_logado', None)
    session.pop('funcionario_logado', None)
    # Redireciona o usuário para a página de login
    return redirect('/')
# Execução do aplicativo Flask
app.run()