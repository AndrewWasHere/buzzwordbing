#
# Copyright 2019 Andrew Lin. All rights reserved.
#
# This software is released under the BSD 3-clause license. See LICENSE.txt or
# https://opensource.org/licenses/BSD-3-Clause for more information.
#
from bingo.game import Game


def test_game_construction():
    """"""
    game = Game()

    assert game.play_by_play == []


def test_game_add_play():
    """"""
    game = Game()

    for idx, play in enumerate(['a', 'b', 'c'], 1):
        game.add_play(play)
        assert len(game.play_by_play) == idx


def test_game_get_plays_all():
    """Test getting all of the play-by-play."""
    game = Game()
    plays = ['a', 'b', 'c']

    for idx, play in enumerate(plays, 1):
        game.add_play(play)
        next_idx, game_plays = game.get_plays(0)
        assert len(game_plays) == idx
        assert idx == next_idx
        assert game_plays == plays[:idx]


def test_game_get_plays_some():
    """Test getting some of the play-by-play."""
    game = Game()
    plays = ['a', 'b', 'c']

    for idx, play in enumerate(plays, 1):
        game.add_play(play)

    for idx in range(len(plays)):
        next_idx, game_plays = game.get_plays(idx)
        assert next_idx == len(plays)
        assert len(game_plays) == len(plays) - idx
        assert game_plays == plays[idx:]


def test_game_get_plays_exceed_range():
    """Test get_plays with index out of range."""
    game = Game()
    plays = ['a', 'b', 'c']

    for idx, play in enumerate(plays, 1):
        game.add_play(play)

    next_idx, game_plays = game.get_plays(len(plays) + 1)
    assert next_idx == len(plays)
    assert game_plays == []
