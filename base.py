from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, ForeignKey, Integer 
import requests
import module

# engine = create_engine(('postgresql://groupe_7:test@localhost:5432/flask_api'))
engine=create_engine('postgresql://groupe7:test_123@localhost:5432/flask_db')
base_session = sessionmaker(bind=engine,autocommit=False,autoflush=False)
 
session = base_session()
 
Base = declarative_base()

Base.metadata.create_all(bind=engine)

def import_api(x):
    Lien0="https://jsonplaceholder.typicode.com/"
    Lien1=Lien0+x
    f=requests.get(Lien1)
    fichier=f.json()
    return fichier

f0=import_api('users')

def utilisateur(liste):

    el=module.User(liste['id'],liste['name'],liste['username'],liste['email'],liste['address']['street'],liste['address']['suite'],liste['address']['city'],liste['address']['zipcode'],
    liste['address']['geo']['lat'],liste['address']['geo']['lng'],liste['phone'], liste['website'],liste['company']['name'],liste['company']['catchPhrase'],liste['company']['bs'],1)
    session.add(el)
    session.commit()

def get_all(info):
    try:
        result = session.query(info).filter_by()
        return result
    except Exception as e:
        print(e)
        return False

def get_user_by_id(id):
    try:
        result = session.query(module.User).filter_by(module.User.id==id).first()
        return result
    except Exception as e:
        print(e)
        return False


def get_todo_by_idUser(id):
    try:
        result = session.query(module.Todo).filter(module.Todo.userId==id).all()
        return result
    except Exception as e:
        print(e)
        return False


