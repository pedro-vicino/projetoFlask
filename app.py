#do módulo flask é importada a biblioteca Flask, a função render_template e o request (solicitação)
from flask import Flask, render_template, request

# classe Produto que é composto pelo construtor init, tendo como atributos nome e quantidade
class Produto :
    def __init__(self, nomeProduto, quantidadeProduto):
        self.nome = nomeProduto
        self.quantidade = quantidadeProduto

# p1 e p2 são instâncias da classe Produto, ou seja, são objetos
p1 = Produto("Panela", 8)
p2 = Produto("Uniforme", 12)
# lista__produtos é uma lista que é composta pelas instâncias p1 e p2
lista_produtos = [p1, p2]

# linha de código que cria uma instância da classe Flask do framework Flask
app = Flask(__name__)

# ('/') é a página principal, rota raiz. Aqui ficará a parte de inserir o item, junto com a lista
@app.route('/')
def lista() :
    return render_template("index.html", todos_produtos = lista_produtos)

@app.route('/', methods=['POST'])
# def cadastro retorna os valores escritos no formulário do index.html
# e a lista__produtos, que é a lista dos objetos p1 e p2
def cadastro() :
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
    return render_template('index.html', todos_produtos = lista_produtos)
app.run()