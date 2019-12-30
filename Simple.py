#Start with python3 Simple.py

from flask import Flask, jsonify, request, make_response
app = Flask(__name__)

@app.route("/")
def hello():
    return "Go Tonto!"

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

@app.route("/next", methods=['GET'])
def cu_mor():
    if request.method != 'GET':
        return make_response('Malformed request', 400)
    headers = {"Content-Type": "application/json"}
    return make_response(jsonify(books), 200, headers)
    #return "Big Dog!"

if __name__ == "__main__":
    app.run(debug=1)