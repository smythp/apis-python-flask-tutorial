import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)

# Later in our code, this function will allow us to return data
# from our database as Python dictionaries, rather than lists.
# When converted to JSON, the dictionary format is generally better for users.
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# At the base URL (/) you would normally have a site with
# info about the project or collection
@app.route('/', methods=['GET'])
def homepage():
    return "An example book catalog API."

# This page is rendered if a resource isn't found
# 404 means "Page not found". 200 means "OK" or "Page found"
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


# Our new API route leaves room in the URL for resources that might
# be added later. It provides a default values of None for ID and genre
# if they aren't provided by the user of the API.
@app.route('/api/v1/resources/books', methods=['GET'])
def api(id=None, genre=None):

    # Get query parameters provided by the user as part of the URL.
    query_parameters = request.args
    id = query_parameters.get('id')
    genre = query_parameters.get('genre')

    # Begin preparing the SQL query that will pull data from the database
    query = 'SELECT * FROM books WHERE '

    # Add ID and genre to the query if they were present in the URL.
    # Return an error if neither ID nor genre are provided.
    if id and genre:
        query += 'id=? and genre=?;'
        to_filter = (id, genre,)
    elif id:
        query += 'id=?;'
        to_filter = (id,)
    elif genre:
        query += 'genre=?;'
        to_filter = (genre,)
    else:
        return page_not_found(404)
    
    # Connect to the database and use our query to grab data as a dictionary
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    results = cur.execute(query, to_filter).fetchall()

    # Convert our data to JSON and return to the user
    return jsonify(results)


app.run()
