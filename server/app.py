from flask import Flask,jsonify,redirect
import json

app = Flask(__name__)

@app.route('/products_list')
def products_list():
    f = open ('products.json', "r")
    products = json.loads(f.read())
    return jsonify(products)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=19002, debug=True)