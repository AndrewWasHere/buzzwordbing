#
# Copyright 2019 Andrew Lin. All rights reserved.
#
# This software is released under the BSD 3-clause license. See LICENSE.txt or
# https://opensource.org/licenses/BSD-3-Clause for more information.
#
import typing
from bingo.board import Board


class Game:
    """Game instance."""
    def __init__(self, buzzwords: typing.List[str], free_space=False):
        """Constructor."""
        self.players = set()
        self.play_by_play = []
        self.board_gen = Board(buzzwords, free_space)
        self.free_space = free_space

    def add_player(self, player) -> None:
        """Add player to game."""
        print(f'Game: new player {player}')
        self.add_play(f"{player} joined the game!")
        self.players.add(player)

    def get_players(self) -> set:
        """Get players in game."""
        return self.players

    def add_play(self, play: str) -> None:
        """Add play to play-by-play."""
        print(f'Game: new play {play}')
        self.play_by_play.append(play)

    def get_plays(self, idx: int) -> typing.Tuple[int, typing.List[str]]:
        """Get plays."""
        last = len(self.play_by_play)
        plays = self.play_by_play[idx:]
        return last, plays

    def make_board(self):
        return self.board_gen.generate()
