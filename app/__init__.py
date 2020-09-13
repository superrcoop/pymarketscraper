from flask import Flask
from app.pyscraper import getInfo, get_all_prices
app = Flask(__name__)
app.config["DEBUG"] = True

app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/api/v1/marketInfo/prices', methods=['GET'])
def all_prices():
    return get_all_prices()


@app.route('/')
def index():
    '''
    A welcome message for the server
    '''
    return getInfo()


if __name__ == "__main__":
    app.run()
