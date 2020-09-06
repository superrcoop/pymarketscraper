from flask import Flask
from pyscraper import getInfo
app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/v1/marketInfo/prices/fruits', methods=['GET'])
def home():
    return getInfo()


app.run()
