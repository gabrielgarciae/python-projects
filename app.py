#objetivo - Criar uma api que disponibiliza a consulta, criação, edição e exclusão de livros
#url base - localhost
#endpoits - 
    # - localhost/livros (get)
    # - localhost/livros/id (get)
    # - localhost/livros/id (put)
    # - localhost/livros/id (delete)
#quais recursos - livros

from flask import Flask, jsonify, request

app = Flask(__name__) #criando uma aplicação com o nome app

livros = [
    {
        'id': 1,
        'titulo': 'Pai Rico e Pai Pobre',
        'autor': 'Robert Kiyosaki e Sharon L. Lechter'
    },
    {
        'id': 2,
        'titulo': 'Sonho Grande',
        'autor': 'Cristiane Correa'
    },
    {
        'id': 3,
        'titulo': 'O Poder da Autorresponsabilidade',
        'autor': 'Paulo Vieira'   
    },
]

#criar API para consultar(todos), consultar id, editar e excluir

#@app.route é a url que a pessoa precisa de digitar para chegar na API livros
#consultar todos
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

#consultar(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
#editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json() #chamadas que o usuário irá fazer
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

#criar
@app.route('/livros', methods=['POST'])
def criar_livros():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

#deletar
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)
#