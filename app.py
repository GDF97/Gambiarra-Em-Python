import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def __fetch_data__(valor):
    url = "https://receitaws.com.br/v1/cnpj/"+valor

    headers = {"Accept": "application/json"}

    response = requests.get(url, headers=headers)

    data = response.json()

    return data


@app.route('/api/GetCNPJ', methods=['POST'])
def __get__cnpj():
    data = request.get_json()
    cnpj = data.get('cnpj')

    return jsonify({"teste":__fetch_data__(cnpj)})

if __name__ == '__main__':
    app.run(debug=True)