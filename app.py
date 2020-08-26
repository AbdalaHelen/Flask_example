from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

games = [
    {'id': 1, 'title': 'The Witcher 3', 'year': '2015', 'read': False},
    {'id': 2, 'title': 'Ori and Blind Forest', 'year': '2015', 'read': True},
    {'id': 3, 'title': 'Little Nightmares', 'year': '2017', 'read': False}
]


@app.route('/')
def hello_world():
    return 'Hello World!!'


@app.route('/games', methods=['GET'])
def games_books():
    return jsonify({'games': games})


@app.route('/games', methods=['GET', 'POST'])
def add_game():
    data = request.get_json()
    newGame = {
        'id': len(games) + 1,
        'title': data['title'],
        'year': data['year'],
        'finished': data['finished']
    }
    games.extend([newGame])
    return jsonify({"Lista de Jogos": games})


@app.route('/game', methods=['PUT'])
def up_games():
    game = (request.get_json())
    for i, u in enumerate(games):
        if u['id'] == game['id']:
            games[i] = game
    return (jsonify({"Message": "Game Updated"}))


@app.route('/game/<id>', methods=['DELETE'])
def delete_games(id):
    for game in games:
        if game['id'] == int(id):
            games.remove(game)
    return (jsonify({"Message": "Game deleted"}))

# del games[game_id]
# return (jsonify({"Message": "Game deleted"}))

# res = make_response(jsonify({"error": "Game not found"}), 404)
# return res


if __name__ == '__main__':
    app.run()
