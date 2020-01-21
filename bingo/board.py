#
# Copyright 2019 Andrew Lin. All rights reserved.
#
# This software is released under the BSD 3-clause license. See LICENSE.txt or
# https://opensource.org/licenses/BSD-3-Clause for more information.
#
import random
import typing


class Board:
    """Bingo board."""
    def __init__(self, buzzwords: typing.List[str], free_space: bool):
        """Constructor."""
        self.buzzwords = buzzwords
        self.free_space = free_space

    def generate(self) -> typing.List:
        print(f"Board: generate() with {len(self.buzzwords)} words\nFree space: {self.free_space}")
        """Generate board."""
        def get_row(idx: int):
            start = 5 * idx
            return shuffled[start: start + 5]

        shuffled = random.sample(self.buzzwords, 25)
        board = [get_row(i) for i in range(5)]

        if self.free_space:
            board[2][2] = 'FREE'

        return board
