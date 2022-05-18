from crypt import methods
import module,base
from flask import Flask, jsonify, request


app = Flask(__name__)
 

@app.route('/api_groupe_7/users', methods=['GET'])
def get_all_users():
    result = base.get_all(module.User)
    
    
    if result:
        return jsonify(status="True", users = base.users(result) )
    
    return jsonify(status="False")

@app.route('/api_groupe_7/users/<int:idUser>', methods=['GET'])
def get_all_user_id(idUser):
    result = base.get_infos_by_id(module.User,idUser)
    print('result : ',result,idUser)
    if result:
        return jsonify(status="True", users = base.users(result) )
    
    return jsonify(status="False")

@app.route('/api_groupe_7/posts', methods=['GET'])
def get_all_post():

    result=base.get_all(module.Post)
    for i in result:
        print(i)
    if result:
        return jsonify(status="True",posts = base.posts(result))
    return jsonify(status="False")

@app.route('/api_groupe_7/posts/<int:postId>', methods=['GET'])
def get_post_by_id(postId):

    result=base.get_infos_by_id(module.Post, postId)
    for i in result:
        print(i)
    if result:
        return jsonify(status="True",posts = base.posts(result))
    return jsonify(status="False")


@app.route('/api_groupe_7/albums', methods=['GET'])
def get_all_album():

    result=base.get_all(module.Album)
    
    if result:
        return jsonify(status="True", albums=base.albums(result))
    
    return jsonify(status="False")

@app.route('/api_groupe_7/albums/<int:albumId>', methods=['GET'])
def get_album_by_id(albumId):

    result=base.get_infos_by_id(module.Album, albumId)
    
    if result:
        return jsonify(status="True", albums=base.albums(result))
    
    return jsonify(status="False")



@app.route('/api_groupe_7/comments', methods=['GET'])
def get_all_comment():

    result=base.get_all(module.Comment)
    
    if result:
        return jsonify(status="True", comments=base.comments(result))
    return jsonify(status="False")

@app.route('/api_groupe_7/comments/<int:commentId>', methods=['GET'])
def get_comment_by_id(commentId):

    result=base.get_infos_by_id(module.Comment, commentId)
    
    if result:
        return jsonify(status="True", comments=base.comments(result))
    return jsonify(status="False")

@app.route('/api_groupe_7/photos', methods=['GET'])
def get_all_photo():

    result=base.get_all(module.Photo)
    
    if result:
        return jsonify(status="True", photos=base.photos(result))
    return jsonify(status="False")

@app.route('/api_groupe_7/photos/<int:photoId>', methods=['GET'])
def get_photo_by_id(photoId):

    result=base.get_infos_by_id(module.Photo, photoId)
    
    if result:
        return jsonify(status="True", photos=base.photos(result))
    return jsonify(status="False")

@app.route('/api_groupe_7/todos', methods=['GET'])
def get_all_todo():

    result=base.get_all(module.Todo)
    
    if result:
        return jsonify(status="True", todos = base.todos(result))
    return jsonify(status="False")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)