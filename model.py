from sqlalchemy import create_engine, Column, String, ForeignKey, Integer , TEXT
import requests
from sqlalchemy.orm import *
import base
from sqlalchemy.orm import *

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
    albums=relationship('Album',cascade="all,delete")
    todos=relationship('Todo',cascade="all,delete")
    posts=relationship('Post',cascade="all,delete")

    
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




class TrashUser(base.Base):
    __tablename__='trashusers'
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
    # trashalbums=relationship('TrashAlbum',cascade="all,delete")
    # trashtodos=relationship('TrashTodo',cascade="all,delete")
    # trashposts=relationship('TrashPost',cascade="all,delete")

    
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


################## ALBUM #################################

class Album(base.Base):
    __tablename__='album'
    userId=Column(Integer,ForeignKey("users.id"))
    id=Column(Integer, primary_key=True)
    title=Column(String(100))
    etat=Column(Integer)
    photos=relationship("Photo",cascade="all,delete")
    def __init__(self, userId, id, title):
        self.userId=userId
        self.id=id
        self.title=title




class TrashAlbum(base.Base):
    __tablename__='trashalbum'
    userId=Column(Integer)
    id=Column(Integer, primary_key=True)
    title=Column(String(100))
    etat=Column(Integer)
    def __init__(self, userId, id, title):
        self.userId=userId
        self.id=id
        self.title=title


################ PHOTOS #######################################

class Photo(base.Base):
    __tablename__='photos'
    albumId=Column(Integer, ForeignKey('album.id', ondelete='CASCADE'))
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

################ TrashPhoto #######################################


class TrashPhoto(base.Base):
    __tablename__='trashphotos'
    albumId=Column(Integer)
    id=Column(Integer, primary_key=True)
    title=Column(String(100))
    url=Column(String(200))
    thumbnailUrl=Column(String(200))
    # etat=Column(Integer)
    def __init__(self, albumId, id, title, url, thumbnailUrl):
        self.albumId=albumId
        self.id=id
        self.title=title
        self.url=url
        self.thumbnailUrl=thumbnailUrl
      ############# TODOS ##############################

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


class TrashTodo(base.Base):
    __tablename__='trashtodo'
    userId=Column(Integer,autoincrement=True)
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
    comments=relationship("Comment",cascade="all,delete")
    def __init__(self, userId, id, title, body):
        self.userId=userId
        self.id=id
        self.title=title
        self.body=body
        


#################################################Corbeille Post
  
class TrashPost(base.Base):
    __tablename__='trashpost'
    userId=Column(Integer)
    id=Column(Integer, primary_key=True)
    title=Column(String(200))
    body=Column(TEXT)
    etat=Column(Integer)
    
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


############# CORBEILLE COMMENTS ##########################

class TrashComment(base.Base):
    __tablename__='trashcomment'
    postId=Column(Integer)
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


# def users(result):
    
#         result= [
#         {
#         "id":user.id,
#         "name":user.name,
#         "username":user.username,
#         "email":user.email,
#         "address":{
#             "street":user.street,
#             "suite":user.suite,
#             "city":user.city,
#             "zipcode":user.zipcode,
#             "geo":{
#                 "lat":user.lat,
#                 "long":user.lng
#             },
#             "phone":user.phone,
#             "websit":user.website
#         },
#         "company":{
#             "name":user.companyName,
#             "catchPhrase":user.catchPhrase,
#             "bs":user.companyBs
#         }
#         } for user in result.all() ]
#         return result


def recupdatauser(data,nuser):
    nuser.name=data.get("name") if data.get("name") else nuser.name
    nuser.username=data.get("username") if data.get("username")else nuser.username
    nuser.suite=data.get("suite") if data.get("suite") else nuser.suite
    nuser.street=data.get("street") if data.get("street") else nuser.street
    nuser.city=data.get("city") if data.get("city") else nuser.street
    nuser.zipcode=data.get("zipcode") if data.get("zipcode") else nuser.zipcode
    nuser.lat=data.get("lat") if data.get("lat") else nuser.lat
    nuser.lng=data.get("lng") if data.get("lng") else nuser.lng
    nuser.phone=data.get("phone") if data.get("phone") else nuser.phone
    nuser.email= data.get("email") if data.get("email") else nuser.email
    nuser.website=data.get("website") if data.get("website") else nuser.website
    nuser.companyName=data.get("companyName") if data.get("companyName") else nuser.companyName
    nuser.catchPhrase=data.get("catchPhrase") if data.get("catchPhrase") else nuser.catchPhrase
    nuser.companyBs=data.get("") if data.get("") else nuser.companyBs


def addtrashpostcom(idUser):
      trashpost=base.session.query(Post).filter(Post.userId==idUser).all()
      for el in trashpost:
        post=TrashPost(el.userId,el.id,el.title,el.body)
        base.session.add(post)
        comment=base.session.query(Comment).filter(Comment.postId==el.id).all()
        for l in comment:
            com=TrashComment(l.postId,l.id,l.name,l.email,l.body)
            base.session.add(com)
        base.session.commit()
            

def addtrashalbumtof(idUser):
    trashalbum=base.session.query(Album).filter(Album.userId==idUser).all()
    for l in trashalbum:
        album=TrashAlbum(l.userId,l.id,l.title)
        base.session.add(album)
        tof=base.session.query(Photo).filter(Photo.albumId==l.id).all()
        for k in tof:
            trashtof=TrashPhoto(k.albumId,k.id,k.title,k.url,k.thumbnailUrl)
            base.session.add(trashtof)
    base.session.commit()
def addtrashtodo(idUser):
    trashtodo=base.session.query(Todo).filter(Todo.userId==idUser).all()
    for m in trashtodo:
        todo=TrashTodo(m.userId,m.id,m.title,m.ETAT)
        base.session.add(todo)
        base.session.commit()

base.initbase()