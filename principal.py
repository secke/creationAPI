from crypt import methods
import module,base
from flask import Flask, jsonify, request


app = Flask(__name__)
 

@app.route('/api_groupe_7/users/', methods=['GET'])
def get_all_users():
    result = base.get_all(module.User)
    if result:
        return jsonify(status="True",
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
    } for user in result.all() ])
    return jsonify(status="False")

@app.route('/api_groupe_7/posts', methods=['GET'])
def get_all_post():

    result=base.get_all(module.Post)
    for post in result:
        print(post)

    if result:
        return jsonify(status="True",
    result=[
        {
           "userId":post.userId,
           "id":post.id,
           "title":post.title,
           "body":post.body
        }for post in result])
    return jsonify(status="False")

@app.route('/api_groupe_7/albums', methods=['GET'])
def get_all_album():

    result=base.get_all(module.Album)
    
    if result:
        return jsonify(status="True",
    result=[
        {
           "userId":album.userId,
           "id":album.id,
           "title":album.title,
        }for album in result])
    return jsonify(status="False")

@app.route('/api_groupe_7/comments', methods=['GET'])
def get_all_comment():

    result=base.get_all(module.Comment)
    
    if result:
        return jsonify(status="True",
    result=[
        {
           "postId":comment.postId,
           "id":comment.id,
           "name":comment.name,
           "email":comment.email,
           "body":comment.body
        }for comment in result])
    return jsonify(status="False")

@app.route('/api_groupe_7/photos', methods=['GET'])
def get_all_photo():

    result=base.get_all(module.Photo)
    
    if result:
        return jsonify(status="True",
    result=[
        {
           "albumId":photo.albumId,
           "id":photo.id,
           "title":photo.title,
           "url":photo.url,
           "thumbnailUrl":photo.thumbnailUrl
        }for photo in result])
    return jsonify(status="False")

@app.route('/api_groupe_7/todos', methods=['GET'])
def get_all_todo():

    result=base.get_all(module.Todo)
    
    if result:
        return jsonify(status="True",
    result=[
        {
           "userId":todo.userId,
           "id":todo.id,
           "title":todo.title,
        #    "completed":todo.completed
        }for todo in result])
    return jsonify(status="False")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)