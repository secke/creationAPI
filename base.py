from builtins import print
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine





engine=create_engine('postgresql://groupe7:test_123@localhost:5432/flask_db')
base_session = sessionmaker(bind=engine,autocommit=False,autoflush=False)
session = base_session()
Base = declarative_base()

def initbase():
    Base.metadata.create_all(bind=engine)



def get_all(info):
    try:
        result = session.query(info).filter_by()
        return result
    except Exception as e:
        print(e)
        return False

def get_infos_by_id(info,id):
    try:
        result = session.query(info).filter_by(id=id)
        return result
    except Exception as e:
        print(e)
        return False

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

def posts(posts):

    posts=[
    {
    "userId":post.userId,
    "id":post.id,
    "title":post.title,
    "body":post.body
    }for post in posts.all()]

    return posts

def albums(albums):
    albums=[
        {
           "userId":album.userId,
           "id":album.id,
           "title":album.title,
        }for album in albums]
    return albums

def comments(comments):
    comments=[
        {
           "postId":comment.postId,
           "id":comment.id,
           "name":comment.name,
           "email":comment.email,
           "body":comment.body
        }for comment in comments]
    return comments

def photos(photos):
    photos=[
        {
           "albumId":photo.albumId,
           "id":photo.id,
           "title":photo.title,
           "url":photo.url,
           "thumbnailUrl":photo.thumbnailUrl
        }for photo in photos]
    return photos

def todos(todos):
    todos=[
        {
           "userId":todo.userId,
           "id":todo.id,
           "title":todo.title,
        #    "completed":todo.completed
        }for todo in todos]
    return todos




def getId(info):
    data=session.query(info).all()
    id=len(data)+1
    return id



def postmethod(requete):
    session.add(requete)
    session.commit()

#########################"

    

    


