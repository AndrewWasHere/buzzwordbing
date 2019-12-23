#
# Copyright 2019 Andrew Lin. All rights reserved.
#
# This software is released under the BSD 3-clause license. See LICENSE.txt or
# https://opensource.org/licenses/BSD-3-Clause for more information.
#
import typing


class Game:
    """Game instance."""
    def __init__(self):
        """Constructor."""
        self.play_by_play = []

    def add_play(self, play: str) -> None:
        """Add play to play-by-play."""
        self.play_by_play.append(play)

    def get_plays(self, idx: int) -> typing.Tuple[int, typing.List[str]]:
        """Get plays."""
        last = len(self.play_by_play)
        plays = self.play_by_play[idx:]

        return last, plays
