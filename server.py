from flask import Flask
import random

app = Flask(__name__)

topics = [
    {'id': 1, 'title': 'Html', 'body': 'Html is ...'},
    {'id': 2, 'title': 'CSS', 'body': 'CSS is ...'},
    {'id': 3, 'title': 'Javascript', 'body': 'Javascript is ...'}
]


@app.route('/')
def index():
    liTags = ''
    for topic in topics:
        liTags = liTags + \
            f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'

    return f'''<!doctype html>
    <html>
      <body>
        <h1><a href="/">WEB</a></h1>
        <ol>
          {liTags}
        </ol>
        <h2>Welcome</h2>
      </body> 
    </html>
    '''


@app.route('/random')
def randomNum():
    return 'random : <stong>' + str(random.random()) + '</strong>'


@app.route('/create/')
def create():
    return 'Create'


@app.route('/read/<id>/')
def read(id):
    # print(id)
    return 'Read ' + id


app.run(debug=True)
