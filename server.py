from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/posts', methods=['GET', 'POST'])
def posts():
    post = [{ 'postId': 0,
      'author': 'Andrew',
      'body': 'Hi',
      'comments': 'Comment'
    }, 
    { 'postId': 1,
      'author': 'Andrew',
      'body': 'Hi2',
      'comments': 'Comment2'
    }]
    return jsonify(post)

@app.route('/api/post/<id>', methods=['GET', 'POST', 'DELETE'])
def post(id):
    print(request)
    return 'hi'

@app.route('/api/comment/<id>')
def comment(id):
  comment = {'uid': 0,
  'author': 'Andrew',
  'body': 'Stuff'}
  return jsonify(comment)

@app.route('/')
def index():
    return render_template('index.html')
