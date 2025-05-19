from flask import Flask
import os
import sys
from Folders import test

app = Flask(__name__)

@app.route('/')
def index():
    folder = test()
    return f'Список папок: {folder}'


if __name__ == '__main__':
    app.run(debug=True)