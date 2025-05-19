from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    req = requests.get('https://google.com')
    data = req.text
    return data

if __name__=='__main__':
    app.run(debug=True)