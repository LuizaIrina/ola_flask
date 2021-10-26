from flask_restful import Resource
from flask import request
import json

lista_habilidades = [{'id': 0, 'name':'Python'},
                     {'id': 1, 'name': 'PHP'},
                     {'id': 2, 'name': 'C++'},
                     {'id': 3, 'name': 'Ruby'},
                     {'id': 4, 'name': 'Java'}]
class Habilidades(Resource):
    def get(self,id):
        return lista_habilidades
    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id]["name"] = dados["name"]
        return lista_habilidades
    def delete(self, id):
        lista_habilidades.pop(id)
        return lista_habilidades
    def post(self,id):
        dados = json.loads(request.data)
        posicao = len(lista_habilidades)
        dados["id"]=posicao
        lista_habilidades.append(dados)
        return lista_habilidades[posicao]