from flask import Flask, jsonify, request, render_template
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

Games = []  # Veriyi saklamak için boş bir liste

@app.route('/')
def home():
    return render_template('index.html')

# Tüm oyunları listele
@app.route('/games', methods=['GET'])
def list_Games():
    return jsonify(Games)

# Yeni bir oyun oluştur
@app.route('/games', methods=['POST'])
def create_Game():
    required_fields = ["Name", "Price", "Publisher", "Release_year", "Version"]
    Game_N = request.json
    if all(field in Game_N for field in required_fields):
        game_id = len(Games) + 1  # Bir sonraki ID'yi belirle
        Game_N["id"] = game_id
        Games.append(Game_N)
        return jsonify(Game_N), 201
    else:
        return jsonify({'error': 'Lütfen tüm gerekli alanları doldurun: Name(string), Price(int), Publisher(string), Release_year(int), Version(int)'}), 400

# Belirli bir oyunu getir
@app.route('/games/<int:id>', methods=['GET'])
def getGame_id(id):
    for game in Games:
        if game['id'] == id:
            return jsonify(game), 200
    return jsonify({'message': 'Bu ID\'ye sahip bir oyun yok!'}), 404

# Belirli bir oyunu güncelle
@app.route('/games/<int:id>', methods=['PUT'])
def update_Game(id):
    for game in Games:
        if game['id'] == id:
            game.update(request.json)
            return jsonify(game), 200
    return jsonify({'message': 'Bu ID\'ye sahip bir oyun yok!'}), 404

# Belirli bir oyunu sil
@app.route('/games/<int:id>', methods=['DELETE'])
def delete_Game(id):
    for game in Games:
        if game['id'] == id:
            Games.remove(game)
            return '', 204
    return jsonify({'message': 'Bu ID\'ye sahip bir oyun yok!'}), 404

if __name__ == '__main__':
    app.run()

