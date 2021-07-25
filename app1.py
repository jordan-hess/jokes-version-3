from flask import Flask
import requests


app = Flask(__name__)

@app.route('/', methods=["GET"])
def get_joke():

    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()

    return "<strong>Chuck Joke:</strong>" + response['value']

if __name__ == '__main__':
    app.debug=True
    app.run()