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
    id=Column(Integer, primary_key=True,autoincrement=True)
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

    
    def __init__(self,id,name,username,email,street,suite,city,zipcode,lat,lng,
        phone, website, companyName,catchPhrase,companyBs):
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
    

    def users(result):
    
        result= [
        {
        "id":user.id,
        "name":user.name,
        "username":user.username,
        "email":user.email,
        "address":{
            "street":user.street,
            "suite":user.suite,
            "city":user.city,
            "zipcode":user.zipcode,
            "geo":{
                "lat":user.lat,
                "long":user.lng
            },
            "phone":user.phone,
            "websit":user.website
        },
        "company":{
            "name":user.companyName,
            "catchPhrase":user.catchPhrase,
            "bs":user.companyBs
        }
        } for user in result.all() ]
        return result

################## ALBUM #################################

class Album(base.Base):
    __tablename__='album'
    userId=Column(Integer)
    id=Column(Integer, primary_key=True)
    title=Column(String(100))
    etat=Column(Integer)
    # photos=relationship("Photo")
    def __init__(self, userId, id, title):
        self.userId=userId
        self.id=id
        self.title=title

################ PHOTOS #######################################

class Photo(base.Base):
    __tablename__='photos'
    albumId=Column(Integer, ForeignKey('album.id'))
    id=Column(Integer, primary_key=True)
    title=Column(String(100))
    url=Column(String(200))
    thumbnailUrl=Column(String(200))
    etat=Column(Integer)
    def __init__(self, albumId, id, title, url, thumbnailUrl):
        self.albumId=albumId
        self.id=id
        self.title=title
        self.url=url
        self.thumbnailUrl=thumbnailUrl
      ############## TODOS ##############################

class Todo(base.Base):
    __tablename__='todo'
    userId=Column(Integer, ForeignKey('users.id'),autoincrement=True)
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
    def __init__(self, userId, id, title, body):
        self.userId=userId
        self.id=id
        self.title=title
        self.body=body
  



############# COMMENTS ##########################

class Comment(base.Base):
    __tablename__='comments'
    postId=Column(Integer, ForeignKey('post.id'))
    id=Column(Integer, primary_key=True)
    name=Column(String(100))
    email=Column(String(100))
    body=Column(TEXT)
    def __init__(self, postId, id, name, email, body):
        self.postId=postId
        self.id=id
        self.name=name
        self.email=email
        self.body=body


