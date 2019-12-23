#
# Copyright 2019 Andrew Lin. All rights reserved.
#
# This software is released under the BSD 3-clause license. See LICENSE.txt or
# https://opensource.org/licenses/BSD-3-Clause for more information.
#
from flask import Flask, request, render_template, abort


class BingoServer(Flask):
    """Bingo Server Front End"""
    def __init__(self, import_name, **kwargs):
        """Constructor."""
        super().__init__(import_name, **kwargs)

        self.games = {"game a": "nil", "game b": "nil"}  # Active games.
        self.buzzwords = []  # list of buzzwords / phrases to use in games.

    def set_buzzwords(self, path: str) -> None:
        """Load buzzwords from file."""
        with open(path, 'r') as fin:
            self.buzzwords = [w for w in fin]


app = BingoServer(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def game_management():
    """Game management page."""
    return render_template("game_management.html", games=sorted(app.games.keys()))


@app.route('/<game_id>/', methods=['GET', 'PUT', 'DELETE'])
def game(game_id):
    """Game page."""
    print(f'game(): hit {game_id}')
    if request.method == 'GET':
        return active_game(game_id)
    elif request.method == 'PUT':
        return new_game(game_id)
    elif request.method == 'DELETE':
        return delete_game(game_id)


@app.route("/favicon.ico/")
def favicon():
    return abort(404)


def active_game(game_id):
    """Serve an active game page."""
    print(f"active game: {game_id} -> {app.games[game_id]}")
    return render_template("player_list.html", game_id=game_id)  # sent to client


def new_game(game_id):
    """Create a new game page."""
    print(f"new game: {game_id}")
    app.games[game_id] = "NotImplemented"
    return f'new game: {game_id}'


def delete_game(game_id):
    """Delete an active game"""
    print(f"delete game: {game_id}")
    del app.games[game_id]
    return f'delete game: {game_id}'


@app.route('/<game_id>/<player_id>/', methods=['GET, POST'])
def player(game_id, player_id):
    """Player page."""
    if request.method == 'GET':
        return player_join(game_id, player_id)
    elif request.method == 'POST':
        return player_move(game_id, player_id)


def player_join(game_id, player_id):
    """Player joins game."""
    return f'{player_id} joined {game_id}'


def player_move(game_id, player_id):
    """Player moves in game."""
    return f'{player_id} moved in {game_id}'

