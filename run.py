from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# @app.route("/<numero>", methods=['GET','POST'])
# def hello(numero):
#     return 'ola mundo....{}'.format(numero)

@app.route("/<int:id>")
def pessoas(id):
    return jsonify({'id':id, 'name':'Rafael'})

@app.route("/soma/<int:valor1>/<int:valor2>")
def soma(valor1, valor2):
    return jsonify({'soma': valor1 + valor2})

@app.route("/somando", methods=['POST'])
def somando():
    dados = json.loads(request.data)
    total = sum(dados['valores'])
    return jsonify({'soma':total})

desenvolvedores = [
    {'id': 0,
     'nome': 'Rafael',
     'habilidades':['Python','C++']
    },
    {'id': 1,
     'nome':'Gabi',
     'habilidades':['Java','C#']
    }
]

# pelo ID devolve, modifica, deleta um desenvolvedor
@app.route("/dev/<int:id>/", methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor ID {} não existe'.format(id)
            response = {'status':'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'status':'erro','mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id]["nome"] = dados["nome"]
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso','mensagem':'Registro excluido'})

# lista todos os desenvolvedores e permite incluir um novo
@app.route('/dev/', methods=['GET','POST'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify({'status':'sucesso','mensagem':'Registro inserido'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)




if __name__ == "__main__":
    app.run(debug=True)