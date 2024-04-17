#do módulo flask é importada a biblioteca Flask, a função render_template e o request (solicitação)
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# linha de código que cria uma instância da classe Flask do framework Flask
app = Flask(__name__)

app.secret_key = 'lojadopedro'

#app.config configura o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD= 'mysql+mysqlconnector',
        usuario= 'root',
        senha= 'cida2011',
        servidor= 'localhost',
        database= 'loja'
    )

#db instacia a class sqlalchemy
db = SQLAlchemy(app)

# classe Produto que é composto pelo construtor init, tendo como atributos nome e quantidade
class Produto(db.Model):
    id_produto = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome_produto = db.Column(db.String(60), nullable=False)
    quantidade_produto = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return '<Name %r>' % self.name

# ('/') é a página principal, rota raiz. Aqui ficará a parte de inserir o item, junto com a lista
@app.route('/lista')
def lista() :
    lista_produtos = Produto.query.order_by(Produto.id_produto)
    return render_template("lista.html", todos_produtos = lista_produtos)

@app.route('/cadastro')
def cadastrar():
    return render_template('cadastro.html')

@app.route('/adiciona', methods=['POST'])
# def cadastro retorna os valores escritos no formulário do index.html
# e a lista__produtos, que é a lista dos objetos p1 e p2
def adiciona() :
    lista_produtos = Produto.query.order_by(Produto.id_produto)
    # nome e quantidade: requisições para obter o 
    # valor submetido com o nome 'txtNome' e 'numQuantidade no formulário.
    nome = request.form['txtNome']
    quantidade = request.form['numQuantidade']
    # requestProduto cria uma nova instância da classe Produto,
    # utilizando os valores nome e quantidade obtidos do formulário
    requestProduto = Produto(nome, quantidade)
    # a instância do produto recém-criada (requestProduto)
    # é adicionada à lista de produtos existentes (lista_produtos).
    lista_produtos.append(requestProduto)

    # renderiza o modelo HTML 'index.html' e passa a lista de produtos (lista_produtos) para o modelo.
    return render_template('lista.html', todos_produtos = lista_produtos)
app.run()