from unittest import result
from model import *
from base import *
from flask import Flask, jsonify, request
import model


app = Flask(__name__)

######################################## USERS##########################################################################
 
@app.route('/api_groupe_7/users', methods=['GET','POST'])
def get_all_users():
    if request.method=='GET':
        result = base.get_all(model.User)
        if result:
            return jsonify(status="True", users = base.users(result) )
        return jsonify(status="False")
    else:
        data=request.get_json()
        id_user=getId(model.User)
        users=model.User(id=id_user,name=data['name'],username=data['username'],email=data["email"],street=data['street'],suite=data['suite'],city=data['city'],zipcode=data["zipcode"],lat=data['lat'],lng=data['lng'],phone=data["phone"],website=data['website'],companyName=data["companyName"],catchPhrase=data["catchPhrase"],companyBs=["companyBs"])
        postmethod(users)
        return "Ok"


@app.route('/api_groupe_7/users/<int:idUser>', methods=['GET','PUT','DELETE'])
def get_all_user_id(idUser):
    if request.method=='GET':
        result = base.get_infos_by_id(model.User,idUser)
        if result:
            return jsonify(status="True", users = base.users(result) )
        
        return jsonify(status="False")
    elif request.method=='PUT':
        data=request.get_json()
        nuser=session.query(User).get(idUser)
        recupdatauser(data,nuser)
        base.session.commit()
        return "Modifié"
    else:
        user=session.query(User).get(idUser)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
        trash=TrashUser(user.id,user.name,user.username,user.email,user.street,user.suite,user.city,user.zipcode,user.lat,user.lng,user.phone,user.website,user.companyName,user.catchPhrase,user.companyBs)
        session.add(trash)
        addtrashpostcom(idUser)
        addtrashalbumtof(idUser)
        addtrashtodo(idUser)
        session.delete(user)
        session.commit()
        return "Supprimé"


@app.route('/api_groupe_7/users/<int:idUser>/albums', methods=['GET','DELETE'])
def get_all_user_id_album(idUser):
    result=session.query(Album).filter(Album.userId==idUser).all()
    if request.method=='GET': 
        if result:
            return jsonify(status="True", albums=base.albums(result))
        
        return jsonify(status="False")
    else:
        addtrashalbumtof(idUser)
        for i in result:
            session.delete(i)
            session.commit()
    return "Supprimé"


@app.route('/api_groupe_7/users/<int:idUser>/photos', methods=['GET','DELETE'])
def get_all_user_id_photos(idUser):
    li=[]
    result1=session.query(Album).filter(Album.userId==idUser).all()
    for i in result1:
        tof=session.query(Photo).filter(Photo.albumId==i.id).all()
        photo=base.photos(tof)
        li.append(photo)
    if request.method=='GET':
        if li:
            return jsonify(status="True", photos=li)
        return jsonify(status="False")
    else:
        for i in result1:
            tof=session.query(Photo).filter(Photo.albumId==i.id).all()
            for k in tof:
                trashtof=TrashPhoto(k.albumId,k.id,k.title,k.url,k.thumbnailUrl)
                session.add(trashtof)
                session.delete(k)
        session.commit()
    return "Supprimé"

@app.route('/api_groupe_7/users/<int:idUser>/comments', methods=['GET','DELETE'])
def get_all_user_id_comments(idUser):
    li=[]
    result1=session.query(Post).filter(Post.userId==idUser).all()
    print(result1)
    for i in result1:
       com=session.query(Comment).filter(Comment.postId==i.id).all()
       com=base.comments(com)
       li.append(com)
    if request.method=='GET':
        if li:
            return jsonify(status="True", comments=li)
        return jsonify(status="False")
    else:
        for i in result1:
            com=session.query(Comment).filter(Comment.postId==i.id).all()
            for k in com:
                trashcom=TrashComment(k.postId,k.id,k.name,k.email,k.body)
                session.add(trashcom)
                session.delete(k)
        session.commit()
    return "Supprimé"
@app.route('/api_groupe_7/users/<int:idUser>/posts', methods=['GET','DELETE'])
def get_all_user_id_posts(idUser):
    result=session.query(Post).filter(Post.userId==idUser)
    if request.method=='GET': 
        if result:
            return jsonify(status="True", posts=base.posts(result))
        return jsonify(status="False")
    else:
        addtrashpostcom(idUser)
        for i in result:
            session.delete(i)
            session.commit()
    return "Supprimé"



######################################################## POSTS##################################################################""

@app.route('/api_groupe_7/posts', methods=['GET','POST'])
def get_all_post():
    if request.method=="GET":
        result=base.get_all(model.Post)
        if result:
            return jsonify(status="True",posts = base.posts(result))
        return jsonify(status="False")
    else:
        data=request.get_json()
        id_post=getId(model.Post)
        post=Post(userId=data["userId"],id=id_post,title=data["title"],body=data["body"])
        postmethod(post)
        return "ok"


@app.route('/api_groupe_7/posts/<int:postId>', methods=['GET','PUT','DELETE'])
def get_post_by_id(postId):
    if request.method=='GET':
        result=base.get_infos_by_id(model.Post, postId)
        if result:
            return jsonify(status="True",posts = base.posts(result))
        return jsonify(status="False")
    elif request.method=='PUT':
        data=request.get_json()
        npost=session.query(Post).get(postId)
        npost.userId=data["userId"]
        npost.title=data["title"]
        npost.body=data["body"]
        session.commit()
        return "okey"
    else:
        npost=session.query(Post).get(postId)
        trash=TrashPost(npost.userId,npost.id,npost.title,npost.body)
        print(trash)
        session.add(trash)
        comment=session.query(Comment).filter(Comment.postId==postId).all()
        for i in comment:
            trashcom=TrashComment(i.postId,i.id,i.name,i.email,i.body)
            session.add(trashcom)
        session.delete(npost)
        session.commit()
        return "okey"


@app.route('/api_groupe_7/posts/<int:postId>/comments', methods=['GET','DELETE'])
def comment_post(postId):
    result=session.query(Comment).filter(Comment.postId==postId).all()
    if request.method=="GET":
        print(result)
        if result:
            return jsonify(status="True",comments = base.comments(result))
        return jsonify(status="False")
    elif request.method=='DELETE':
        for i in result:
            trash=TrashComment(i.postId,i.id,i.name,i.email,i.body)
            session.add(trash)
            session.delete(i)
            session.commit()
    return "Suppression reussie"









########################################################## COMMMENT #############################################################
@app.route('/api_groupe_7/comments', methods=['GET','POST'])
def get_all_comment():
    if request.method=='GET':
        result=base.get_all(model.Comment)
        
        if result:
            return jsonify(status="True", comments=base.comments(result))
        return jsonify(status="False")
    else:
        data=request.get_json()
        id_comment=getId(model.Comment)
        comment=Comment(postId=data["postId"],id=id_comment,name=data["name"],email=data["email"],body=data["body"])
        postmethod(comment)
        return "ok"

@app.route('/api_groupe_7/comments/<int:commentId>', methods=['GET','PUT','DELETE'])
def get_comment_by_id(commentId):
    if request.method=='GET':
        result=base.get_infos_by_id(model.Comment, commentId)
        if result:
            return jsonify(status="True", comments=base.comments(result))
        return jsonify(status="False")
    elif request.method=='PUT':
        data=request.get_json()
        ncom=session.query(Comment).get(commentId)
        ncom.body=data["body"]
        ncom.email=data["email"]
        ncom.name=data["name"]
        ncom.postId=data["postId"]
        session.commit()
        return "Succesful"
    
    elif request.method=='DELETE':
            result=session.query(Comment).get(commentId)
            trash=TrashComment(result.postId,result.id,result.name,result.email,result.body)
            session.add(trash)
            session.delete(result)
            session.commit()
    return "Suppression reussi"





############################################################ ALBUMS ######################################################################""
@app.route('/api_groupe_7/albums', methods=['GET','POST'])
def get_all_album():
    if request.method=='GET':
        result=base.get_all(model.Album)
        
        if result:
            return jsonify(status="True", albums=base.albums(result))
        
        return jsonify(status="False")
    else:
        data=request.get_json()
        id_album=getId(model.Album)
        album=Album(userId=data["userId"],id=id_album,title=data["title"])
        postmethod(album)
        return "ok"


@app.route('/api_groupe_7/albums/<int:albumId>', methods=['GET'])
def get_album_by_id(albumId):

    result=base.get_infos_by_id(model.Album, albumId)
    
    if result:
        return jsonify(status="True", albums=base.albums(result))
    
    return jsonify(status="False")


###################################################################### PHOTOS##############################################################
@app.route('/api_groupe_7/photos', methods=['GET'])
def get_all_photo():

    result=base.get_all(model.Photo)
    
    if result:
        return jsonify(status="True", photos=base.photos(result))
    return jsonify(status="False")

@app.route('/api_groupe_7/photos/<int:photoId>', methods=['GET'])
def get_photo_by_id(photoId):

    result=base.get_infos_by_id(model.Photo, photoId)
    
    if result:
        return jsonify(status="True", photos=base.photos(result))
    return jsonify(status="False")

@app.route('/api_groupe_7/todos', methods=['GET','POST'])
def get_all_todo():
    if request.method=='GET':
        result=base.get_all(model.Todo)
        
        if result:
            return jsonify(status="True", todos = base.todos(result))
        return jsonify(status="False")
    else:
        data=request.get_json()
        id_todo=getId(Todo)
        todo=Todo(id=id_todo ,userId=data["userId"],title=data["title"],ETAT=data["ETAT"])
        postmethod(todo)
        return "Ok"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)