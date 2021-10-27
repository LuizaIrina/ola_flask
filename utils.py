from models import Pessoas, db_session

def insere_pessoas():
    pessoa = Pessoas(nome='Rafael', idade=45)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    #filter_by retorna uma lista de objetos, por isso devemos percorrer com for
    pessoa = Pessoas.query.filter_by(nome='Rafael')
    for p in pessoa:
        print(p)
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    print(pessoa.idade)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    pessoa.idade = 21
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    pessoa.delete()

if __name__=='__main__':
    #insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()