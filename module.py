
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, ForeignKey, Integer , TEXT
import requests
import base

# engine = create_engine(('postgresql://groupe_7:test@localhost:5432/flask_api'))
# base_session = sessionmaker(bind=engine,autocommit=False,autoflush=False)
 
# session = base_session()
 
# Base = declarative_base()


class User(base.Base):
    __tablename__='users'
    id=Column(Integer, primary_key=True)
    name=Column(String(50))
    username=Column(String(50))
    email=Column(String(50))
    street=Column(String(200))
    suite=Column(String(200))
    city=Column(String(200))
    zipcode=Column(String(200))
    lat=Column(String(50))
    lng=Column(String(50))
    phone=Column(String(50))
    website=Column(String(100))
    companyName=Column(String(400))
    catchPhrase=Column(String(400))
    companyBs=Column(String(400))
    etat=Column(Integer)
    
    def __init__(self,id,name,username,email,street,suite,city,zipcode,lat,lng,
    phone, website, companyName,catchPhrase,companyBs,etat):
        self.id=id
        self.name=name
        self.username=username
        self.email=email
        self.street=street
        self.suite=suite
        self.city=city
        self.zipcode=zipcode
        self.lat=lat
        self.lng=lng
        self.phone=phone
        self.website=website
        self.companyName=companyName
        self.catchPhrase=catchPhrase
        self.companyBs=companyBs
        self.etat=etat

################## ALBUM #################################

class Album(base.Base):
    __tablename__='album'
    userId=Column(Integer)
    id=Column(Integer, primary_key=True)
    title=Column(String(100))
    etat=Column(Integer)
    # photos=relationship("Photo")
    def __init__(self, userId, id, title,etat):
        self.userId=userId
        self.id=id
        self.title=title
        self.etat=etat

################ PHOTOS #######################################

class Photo(base.Base):
    __tablename__='photos'
    albumId=Column(Integer, ForeignKey('album.id'))
    id=Column(Integer, primary_key=True)
    title=Column(String(100))
    url=Column(String(200))
    thumbnailUrl=Column(String(200))
    etat=Column(Integer)
    def __init__(self, albumId, id, title, url, thumbnailUrl,etat):
        self.albumId=albumId
        self.id=id
        self.title=title
        self.url=url
        self.thumbnailUrl=thumbnailUrl
        self.etat=etat

############## TODOS ##############################

class Todo(base.Base):
    __tablename__='todo'
    userId=Column(Integer, ForeignKey('users.id'))
    id=Column(Integer, primary_key=True)
    title=Column(String(200))
    ETAT=Column(TEXT)
    
    # completed=Column(Boolean)
    def __init__(self,userId, id, title, ETAT):
        self.userId=userId
        self.id=id
        self.title=title
        self.ETAT=ETAT

############## POST ########################

class Post(base.Base):
    __tablename__='post'
    userId=Column(Integer, ForeignKey('users.id'))
    id=Column(Integer, primary_key=True)
    title=Column(String(200))
    body=Column(TEXT)
    etat=Column(Integer)
    # comments=relationship("Comment")
    def __init__(self, userId, id, title, body,etat):
        self.userId=userId
        self.id=id
        self.title=title
        self.body=body
        self.etat=etat



############# COMMENTS ##########################

class Comment(base.Base):
    __tablename__='comments'
    postId=Column(Integer, ForeignKey('post.id'))
    id=Column(Integer, primary_key=True)
    name=Column(String(100))
    email=Column(String(100))
    body=Column(TEXT)
    etat=Column(Integer)
    def __init__(self, postId, id, name, email, body,etat):
        self.postId=postId
        self.id=id
        self.name=name
        self.email=email
        self.body=body
        self.etat=etat
        # self.password=password


############Connexion############################

class Connexion(base.Base):
    __tablename__='connexions'
    id=Column(Integer, primary_key=True,autoincrement=True)
    login=Column(String(50))
    password=Column(String(50))
    id_user=Column(Integer,ForeignKey('users.id')) 
    # users=relationship("User",back_populates="connexions")

    def __init__(self ,login,password,id_user):
        self.login=login
        self.password=password
        self.id_user=id_user


    # Base.metadata.create_all(bind=engine)


# def import_api(x):
#     Lien0="https://jsonplaceholder.typicode.com/"
#     Lien1=Lien0+x
#     f=requests.get(Lien1)
#     fichier=f.json()
#     return fichier

# f0=User.import_api('users')

# def utilisateur(liste):

#     el=User(liste['id'],liste['name'],liste['username'],liste['email'],liste['address']['street'],liste['address']['suite'],liste['address']['city'],liste['address']['zipcode'],
#     liste['address']['geo']['lat'],liste['address']['geo']['lng'],liste['phone'], liste['website'],liste['company']['name'],liste['company']['catchPhrase'],liste['company']['bs'],1)
#     base.session.add(el)
#     base.session.commit()

# def get_all(info):
#     try:
#         result = base.session.query(info).filter_by()
#         return result
#     except Exception as e:
#         print(e)
#         return False

# def get_user_by_id(id):
#     try:
#         result = base.session.query(User).filter_by(User.id==id).first()
#         return result
#     except Exception as e:
#         print(e)
#         return False

# # def add_user(email, nom, prenom, ville, telephone):
# #     try:
# #         user = User(email=email,
# #         nom=nom,
# #         prenom=prenom,
# #         ville=ville,
# #         telephone=telephone)
# #         session.add(user)
# #         session.commit()
 
# #         return True
 
# #     except Exception as e:
# #         print(e)
    
# #         return False
 
# # 
 
 
# # def delete_user_by_id(email):
# #     try:
# #         user_to_delete = get_user_by_id(email)
# #         if user_to_delete :
# #             session.delete(user_to_delete)
# #             session.commit()
# #             return True
# #         else:
# #             return False
# #     except Exception as e:
# #         print(e)
# #         return False
 
# # def update_attribute(email, attributes):
 
# #     try:
# #         user_to_update = get_user_by_id(email)
# #         if user_to_update :
# #             for k,v in attributes.items():
# #                 setattr(user_to_update, k, v)
# #                 session.commit()
# #             return user_to_update
# #         else:
#             return False
#     except Exception as e:
#         print(e)
#         return False

