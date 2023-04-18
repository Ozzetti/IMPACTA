from flask import Flask, jsonify, make_response

tenis = [
    {
      'marca':'nike',
      'nome':'nike preta'
    },
    {
      'marca':'nike',
      'nome':'nike branca'
    },
    {
      'marca':'nike',
      'nome':'nike laranja'
    },
    {
      'marca':'adidas',
      'nome':'adidas vermelha'
    },
    {
      'marca':'adidas',
      'nome':'adidas cinza'
    },
    {
      'marca':'puma',
      'nome':'puma verde'
    },
    {
      'marca':'puma',
      'nome':'puma azul'
    }
]

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Olá, você pode acessar a URI de /buscas/', 200

@app.route('/busca', methods=['GET'])
def search():
    return 'Utilize /tenis para verificar as tenis disponíveis', 200

@app.route('/busca/tenis', methods=['GET'])
def showall():
    return jsonify(tenis), 200

@app.route('/busca/tenis/<string:marca>', methods=['GET'])
def searchbootbrand(marca):
    list = []

    for tenis in tenis:
        if tenis.get('marca') == marca:
            list.append(tenis)

    return jsonify(list), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
