from model import *
from base import *
from flask import Flask, jsonify, request
# import model


app = Flask(__name__)

######################################## USERS##########################################################################
 
@app.route('/api_groupe_7/users', methods=['GET','POST'])
def get_all_users():
    if request.method=='GET':
        result = model.base.get_all(model.User)
        if result:
            return jsonify(status="True", users = model.base.users(result) )
        return jsonify(status="False")
    else:
        data=request.get_json()
        id_user=getId(model.User)
        users=model.User(id=id_user,name=data['name'],username=data['username'],email=data["email"],street=data['street'],suite=data['suite'],city=data['city'],zipcode=data["zipcode"],lat=data['lat'],lng=data['lng'],phone=data["phone"],website=data['website'],companyName=data["companyName"],catchPhrase=data["catchPhrase"],companyBs=["companyBs"])
        postmethod(users)
        return "Ok"


@app.get('/api_groupe_7/users/<int:idUser>')
def get_all_user_id(idUser):
    result = model.base.get_infos_by_id(model.User,idUser)
    print('result : ',result,idUser)
    if result:
        return jsonify(status="True", users = model.base.users(result) )
    
    return jsonify(status="False")

######################################################## POSTS##################################################################""

@app.route('/api_groupe_7/posts', methods=['GET','POST'])
def get_all_post():
    if request.method=="GET":
        result=model.base.get_all(model.Post)
        for i in result:
            print(i)
        if result:
            return jsonify(status="True",posts = model.base.posts(result))
        return jsonify(status="False")
    else:
        data=request.get_json()
        id_post=getId(model.Post)
        post=Post(userId=data["userId"],id=id_post,title=data["title"],body=data["body"])
        base.session.add(post)
        base.session.commit()
        postmethod(post)
        return "ok"


@app.route('/api_groupe_7/posts/<int:postId>', methods=['GET','PUT','DELETE'])
def get_post_by_id(postId):
    if request.method=='GET':
        result=model.base.get_infos_by_id(model.Post, postId)
        print(result)
        if result:
            return jsonify(status="True",posts = model.base.posts(result))
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
        session.add(trash)
        comment=session.query(Comment).filter(Comment.postId==postId).all()
        for i in comment:
             session.delete(i)
        session.delete(npost)
        session.commit()
        return "okey"


########################################################## COMMMENT #############################################################
@app.route('/api_groupe_7/comments', methods=['GET','POST'])
def get_all_comment():
    if request.method=='GET':
        result=model.base.get_all(model.Comment)
        
        if result:
            return jsonify(status="True", comments=model.base.comments(result))
        return jsonify(status="False")
    else:
        data=request.get_json()
        id_comment=getId(model.Comment)
        comment=Comment(postId=data["postId"],id=id_comment,name=data["name"],email=data["email"],body=data["body"])
        postmethod(comment)
        return "ok"

@app.route('/api_groupe_7/comments/<int:commentId>', methods=['GET'])
def get_comment_by_id(commentId):

    result=model.base.get_infos_by_id(model.Comment, commentId)
    
    if result:
        return jsonify(status="True", comments=model.base.comments(result))
    return jsonify(status="False")


############################################################ ALBUMS ######################################################################""
@app.route('/api_groupe_7/albums', methods=['GET','POST'])
def get_all_album():
    if request.method=='GET':
        result=model.base.get_all(model.Album)
        
        if result:
            return jsonify(status="True", albums=model.base.albums(result))
        
        return jsonify(status="False")
    else:
        data=request.get_json()
        id_album=getId(model.Album)
        album=Album(userId=data["userId"],id=id_album,title=data["title"])
        postmethod(album)
        return "ok"


@app.route('/api_groupe_7/albums/<int:albumId>', methods=['GET','PUT','DELETE'])
def get_album_by_id(albumId):
    result=model.base.get_infos_by_id(model.Album, albumId)
    if request.method=='GET':
    
        if result:
            return jsonify(status="True", albums=model.base.albums(result))
        
        return jsonify(status="False")

    elif request.method=='PUT':
        data = request.get_json()
        nalbum=session.query(Album).get(albumId)
        nalbum.title=data['title']
        nalbum.id=data['id']
        nalbum.userId=data["userId"]
        session.commit()
        return 'Bingo'
    else:
        nalbum=session.query(Album).get(albumId)
        try:
            trashalbum=TrashAlbum( nalbum.userId, nalbum.id, nalbum.title)
            session.add(trashalbum)
            session.delete(nalbum)
            session.commit()
        except:
            session.delete(nalbum)
            session.commit()
            pass

        photos=session.query(Photo).filter(Photo.albumId==albumId).all()

        for photo in photos:
            trashphoto=TrashPhoto(photo.albumId, photo.id, photo.title, photo.url, photo.thumbnailUrl)
            try:
                session.add(trashphoto)
                session.delete(photo)

                session.commit()
            except :
                print('e')
                pass
        return 'Bingo'



###################################################################### PHOTOS##############################################################
@app.route('/api_groupe_7/photos', methods=['GET'])
def get_all_photo():

    result=model.base.get_all(model.Photo)
    
    if result:
        return jsonify(status="True", photos=model.base.photos(result))
    return jsonify(status="False")

@app.route('/api_groupe_7/photos/<int:photoId>', methods=['GET', 'PUT', 'DELETE'])
def get_photo_by_id(photoId):
    if request.method=='GET':
        result=model.base.get_infos_by_id(model.Photo, photoId)
        
        if result:
            return jsonify(status="True", photos=model.base.photos(result))
        return jsonify(status="False")
    elif request.method=='PUT':
        data = request.get_json()
        nphoto=session.query(Photo).get(photoId)
        nphoto.title=data['title']
        nphoto.id=data['id']
        nphoto.albumId=data["albumId"]
        nphoto.url=data["url"]
        nphoto.thumbnailUrl=data["thumbnailUrl"]
        session.commit()
        return 'Bingo'
    else:
        nphoto=session.query(Photo).get(photoId)
        session.add(nphoto)
        session.delete(nphoto)
        session.commit()
        return 'Bingo'


@app.route('/api_groupe_7/todos', methods=['GET','POST'])
def get_all_todo():
    if request.method=='GET':
        result=model.base.get_all(model.Todo)
        
        if result:
            return jsonify(status="True", todos = model.base.todos(result))
        return jsonify(status="False")
    else:
        data=request.get_json()
        id_todo=getId(Todo)
        todo=Todo(id=id_todo ,userId=data["userId"],title=data["title"],ETAT=data["ETAT"])
        postmethod(todo)
        return "Ok"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)