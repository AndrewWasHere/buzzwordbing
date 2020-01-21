#
# Copyright 2019 Andrew Lin. All rights reserved.
#
# This software is released under the BSD 3-clause license. See LICENSE.txt or
# https://opensource.org/licenses/BSD-3-Clause for more information.
#
from flask import Flask, request, render_template, abort, redirect
from bingo.game import Game


class BingoServer(Flask):
    """Bingo Server Front End"""
    def __init__(self, import_name, **kwargs):
        """Constructor."""
        super().__init__(import_name, **kwargs)

        self.games = {}  # Active games.
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
    if request.method == 'GET':
        return active_game(game_id)
    elif request.method == 'PUT':
        print(f"PUT, got {request.form['free']}")
        return new_game(game_id)
    elif request.method == 'DELETE':
        return delete_game(game_id)


@app.route('/<game_id>/play-by-play/', methods=['POST'])
def play_by_play(game_id):
    """Play-by-play."""
    selected = app.games[game_id]

    def unpack_request():
        data = request.form
        try:
            print(f"index: {data['idx']}")
            return int(data["idx"])
        except KeyError:
            print("No idx supplied")
            # Didn't supply an index.
            return 0

    new_idx, plays = selected.get_plays(unpack_request())
    return render_template("play_by_play.txt", new_idx=new_idx, plays=plays)


@app.route("/favicon.ico/")
def favicon():
    return abort(404)


def active_game(game_id):
    """Serve an active game page."""
    try:
        return render_template("player_list.html",
                               game_id=game_id,
                               game=app.games[game_id],
                               free_spaces=app.games[game_id].free_space)  # sent to client
    except KeyError:
        # Somebody thought there was a game named this, but there wasn't.
        return redirect("/")


def new_game(game_id):
    """Create a new game page."""
    free_spaces = False
    if request.form['free'] == "true":
        free_spaces = True
    app.games[game_id] = Game(app.buzzwords, free_spaces)
    return f'new game: {game_id}'


def delete_game(game_id):
    """Delete an active game"""
    del app.games[game_id]
    return f'delete game: {game_id}'


@app.route('/<game_id>/<player_id>/', methods=['GET', 'POST'])
def player(game_id, player_id):
    """Player page."""
    try:
        if request.method == 'GET':
            return player_join(game_id, player_id)
        elif request.method == 'POST':
            print(player_id)
            if player_id != "play-by-play":
                return player_move(game_id, player_id)
            else:
                return play_by_play(game_id)
    except KeyError:
        #  The game was suddenly deleted for no apparent reason.
        return redirect("/")


def player_join(game_id, player_id):
    """Player joins game."""
    app.games[game_id].add_player(player_id)
    board = app.games[game_id].make_board()
    return render_template("gameboard.html", board=board, game_id=game_id, player_id=player_id)


def player_move(game_id, player_id):
    """Player moves in game."""
    move = request.form["move"]
    full_text = f"{player_id} {move}"
    app.games[game_id].add_play(full_text)
    return f'{player_id} moved in {game_id}: {move}'

