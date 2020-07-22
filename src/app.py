from flask import Flask, request
import json


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return Null
    
if __name__ == "__main__":
    app.run(debug=True)
