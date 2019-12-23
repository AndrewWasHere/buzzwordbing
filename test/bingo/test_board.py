#
# Copyright 2019 Andrew Lin. All rights reserved.
#
# This software is released under the BSD 3-clause license. See LICENSE.txt or
# https://opensource.org/licenses/BSD-3-Clause for more information.
#
from collections import defaultdict

import pytest

from bingo.board import Board


@pytest.fixture
def buzzwords():
    """Buzzwords."""

    # Assumes running tests from project root!
    with open('buzzwords.txt', 'r') as fin:
        bw = [w for w in fin]

    assert '' not in bw

    return bw


def test_board_construction(buzzwords):
    """"""
    free_space = True

    board = Board(buzzwords, free_space)

    assert board.buzzwords == buzzwords
    assert board.free_space == free_space


def test_board_generate_free_space(buzzwords):
    """Test board generation with free space."""
    words = defaultdict(int)
    board = Board(buzzwords, True).generate()

    assert isinstance(board, list)
    assert len(board) == 5
    for row in board:
        assert len(row) == 5
        for word in row:
            assert word in buzzwords or word == 'FREE'
            words[word] += 1
            assert words[word] == 1  # word is unique

    assert board[2][2] == 'FREE'


def test_board_generate_no_free_space(buzzwords):
    """Test board generation with no free space"""
    words = defaultdict(int)
    board = Board(buzzwords, False).generate()

    assert isinstance(board, list)
    assert len(board) == 5
    for row in board:
        assert len(row) == 5
        for word in row:
            assert word in buzzwords
            words[word] += 1
            assert words[word] == 1  # word is unique
