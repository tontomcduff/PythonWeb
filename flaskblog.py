#Start with python3 flaskblog.py

from flask import Flask, make_response, request, jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '<h1>Home Page</h1>'

@app.route('/about')
def about():
    return '<h1>About Page</h1>'

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]    

@app.route('/api/v1/data/all', methods=['GET'])
#method gets all data
def get_data_all():
    #heads = {"Content-Type": "application/json"}
    return jsonify(books)

@app.route('/api/v1/data', methods=['GET'])
#method to get a single data item
def get_data():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id supplied."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)

