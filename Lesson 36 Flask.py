from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Hello'
    return name

if __name__ == '__main__':
    app.run(debug=True)