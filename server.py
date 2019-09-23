from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

db = {
    'posts': 
      [{ 
        'postId': 0,
        'author': 'Andrew',
        'body': 'Hi',
        'comments': 'Comment'
      }, 
      { 'postId': 1,
        'author': 'Andrew',
        'body': 'Hi2',
        'comments': 'Comment2'
      }], 
    'comments': 
      [{
        'commentId': 0,
        'uid': 0,
        'author': 'Andrew',
        'body': 'Stuff'
      }]
    }

@app.route('/api/posts', methods=['GET', 'POST'])
def posts():
    return jsonify(db.posts)

@app.route('/api/post/<id>', methods=['GET', 'POST', 'DELETE'])
def post(id):
    return 'hi'

@app.route('/api/comment/<id>')
def comment(id):
  return jsonify(db.comments)

@app.route('/')
def index():
    return render_template('index.html')
