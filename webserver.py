# -*- coding: utf-8 -*-
from flask import Flask, jsonify

#run this program and browse to http://127.0.0.1:5000/books to see the response.

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'Why Software Sucks (and what you can do about it)',
        'author': 'Platt, David S.', 
        'available': True
    },
    {
        'id': 2,
        'title': 'Introduction to Pyhton Programming',
        'author': 'Smith, Valerie', 
        'available': False
    },
    {
        'id': 3,
        'title': 'My Book',
        'author': 'Me', 
        'available': False
    }
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': books})

if __name__ == '__main__':
    app.run(debug=True)