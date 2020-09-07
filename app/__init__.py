from flask import Flask
from app.pyscraper import getInfo
app = Flask(__name__)


@app.route('/api/v1/marketInfo/prices/fruits', methods=['GET'])
def home():
    return getInfo()

# A welcome message to test our server


@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"
