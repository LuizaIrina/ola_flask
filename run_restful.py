from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json



app = Flask(__name__)
api = Api(app)

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
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor ID {} não existe'.format(id)
            response = {'status':'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido'
            response = {'status':'erro','mensagem': mensagem}
        return response
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status':'sucesso','mensagem':'Registro excluido'}


# lista todos os desenvolvedores e permite incluir um novo
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)