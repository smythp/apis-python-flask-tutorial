import flask
from flask import request, jsonify

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return "Hello there"


@app.route('/api/1.0', methods=['GET'])
def api_root():

    books = [
        {'id': 0,
         'name': 'The Once and Future King',
         'Author': 'E. B. White'},
        {'id': 1,
         'name': 'Mansfield Park',
         'author': 'Jane Austen'},
        {'id': 2,
         'name': 'Flask Web Development',
         'author': 'Miguel Grinberg'},
    ]

    id = int(request.args['id'])

    [print(type(book['id'])) for book in books]

    matched_books = [book for book in books if book['id'] == id]

    print(matched_books)
    
    if 'id' in request.args:

        return jsonify(books)

    else:
        return "Malformed request. Please try again."


app.run()
