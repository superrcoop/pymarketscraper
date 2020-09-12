from flask import Flask
from app.pyscraper import getInfo, get_all_prices, get_fruits_prices
app = Flask(__name__)
app.config["DEBUG"] = True

app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/api/v1/marketInfo/prices/fruits', methods=['GET'])
def fruits_prices():
    return get_fruits_prices()


@app.route('/api/v1/marketInfo/prices/herbs', methods=['GET'])
def herbs_prices():
    return get_herbs_prices()


@app.route('/api/v1/marketInfo/prices/legumes', methods=['GET'])
def legumes_prices():
    return get_legumes_prices()


@app.route('/api/v1/marketInfo/prices/vegetable', methods=['GET'])
def vegetables_prices():
    return get_vegetable_prices()


@app.route('/api/v1/marketInfo/prices/crops', methods=['GET'])
def crops_prices():
    return get_crops_prices()


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
