from crypt import methods
from model import *
from base import *
from flask import Flask, jsonify, request
import model


app = Flask(__name__)
 
@app.route('/api_groupe_7/users', methods=['GET'])
def get_all_users():
    result = model.base.get_all(model.User)

    
    if result:
        return jsonify(status="True", users = model.base.users(result) )
    
    return jsonify(status="False")

@app.route('/api_groupe_7/users/<int:idUser>', methods=['GET'])
def get_all_user_id(idUser):
    result = model.base.get_infos_by_id(model.User,idUser)
    print('result : ',result,idUser)
    if result:
        return jsonify(status="True", users = model.base.users(result) )
    
    return jsonify(status="False")

@app.route('/api_groupe_7/posts', methods=['GET'])
def get_all_post():

    result=model.base.get_all(model.Post)
    for i in result:
        print(i)
    if result:
        return jsonify(status="True",posts = model.base.posts(result))
    return jsonify(status="False")

@app.route('/api_groupe_7/posts/<int:postId>', methods=['GET'])
def get_post_by_id(postId):

    result=model.base.get_infos_by_id(model.Post, postId)
    for i in result:
        print(i)
    if result:
        return jsonify(status="True",posts = model.base.posts(result))
    return jsonify(status="False")


@app.route('/api_groupe_7/albums', methods=['GET'])
def get_all_album():

    result=model.base.get_all(model.Album)
    
    if result:
        return jsonify(status="True", albums=model.base.albums(result))
    
    return jsonify(status="False")

@app.route('/api_groupe_7/albums/<int:albumId>', methods=['GET'])
def get_album_by_id(albumId):

    result=model.base.get_infos_by_id(model.Album, albumId)
    
    if result:
        return jsonify(status="True", albums=model.base.albums(result))
    
    return jsonify(status="False")



@app.route('/api_groupe_7/comments', methods=['GET'])
def get_all_comment():

    result=model.base.get_all(model.Comment)
    
    if result:
        return jsonify(status="True", comments=model.base.comments(result))
    return jsonify(status="False")

@app.route('/api_groupe_7/comments/<int:commentId>', methods=['GET'])
def get_comment_by_id(commentId):

    result=model.base.get_infos_by_id(model.Comment, commentId)
    
    if result:
        return jsonify(status="True", comments=model.base.comments(result))
    return jsonify(status="False")

@app.route('/api_groupe_7/photos', methods=['GET'])
def get_all_photo():

    result=model.base.get_all(model.Photo)
    
    if result:
        return jsonify(status="True", photos=model.base.photos(result))
    return jsonify(status="False")

@app.route('/api_groupe_7/photos/<int:photoId>', methods=['GET'])
def get_photo_by_id(photoId):

    result=model.base.get_infos_by_id(model.Photo, photoId)
    
    if result:
        return jsonify(status="True", photos=model.base.photos(result))
    return jsonify(status="False")

@app.route('/api_groupe_7/todos', methods=['GET'])
def get_all_todo():

    result=model.base.get_all(model.Todo)
    
    if result:
        return jsonify(status="True", todos = model.base.todos(result))
    return jsonify(status="False")

##################################################### Method POST#####################################################


############################################### User#############################################################################
@app.route('/api_groupe_7/users', methods=['POST'])
def post_user():
    data=request.get_json()
    id_user=getId(model.User)
    users=model.User(id=id_user,name=data['name'],username=data['username'],email=data["email"],street=data['street'],suite=data['suite'],city=data['city'],zipcode=data["zipcode"],lat=data['lat'],lng=data['lng'],phone=data["phone"],website=data['website'],companyName=data["companyName"],catchPhrase=data["catchPhrase"],companyBs=["companyBs"])
    session.add(users)
    session.commit()
    session.close()
    return "Ok"




######################################## Posts "####################################################################################

@app.route('/api_groupe_7/posts', methods=['POST'])
def post_posts():
    data=request.get_json()
    id_post=getId(model.Post)
    post=Post(userId=data["userId"],id=id_post,title=data["title"],body=data["body"])
    session.add(post)
    session.commit()
    session.close()
    return "ok"



##################################### ALBUMS #########################################################################################

@app.route('/api_groupe_7/albums', methods=['POST'])
def post_albums():
    data=request.get_json()
    id_album=getId(model.Album)
    album=Album(userId=data["userId"],id=id_album,title=data["title"])
    session.add(album)
    session.commit()
    session.close()
    return "ok"



#######################################comment##############################################################""

@app.route('/api_groupe_7/comments', methods=['POST'])
def post_comment():
    data=request.get_json()
    id_comment=getId(model.Comment)
    comment=Comment(postId=data["postId"],id=id_comment,name=data["name"],email=data["email"],body=data["body"])
    session.add(comment)
    session.commit()
    session.close()
    return "ok"




####################################### Photo ##############################################################""

@app.route('/api_groupe_7/photos', methods=['POST'])
def post_photo():
    data=request.get_json()
    id_photo=getId(model.Photo)
    photo=Photo(albumId=data["albumId"],id=id_photo,title=data["title"],url=data["url"],thumbnailUrl=data["thumbnailUrl"])
    session.add(photo)
    session.commit()
    session.close()
    return "ok"




############################################## Todo#####################################################################################
@app.route('/api_groupe_7/todos', methods=['POST'])
def post_todo():
    data=request.get_json()
    id_todo=getId(Todo)
    todo=Todo(id=id_todo ,userId=data["userId"],title=data["title"],ETAT=data["ETAT"])
    session.add(todo)
    session.commit()
    session.close()
    return "Ok"



@app.route("/")
def test():
    
    return "Hey"

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)