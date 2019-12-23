Design
======

Buzzword Bingo is web-based, capable of hosting multiple games of buzzword
bingo at one time. Since this is a "friendly" game, it is run on the honor
system -- the player is responsible for keeping track of its own board, and
whether or not a bingo is achieved.

Players report all moves and bingos to the host.

.. uml::
   :caption: Class Diagram

    @startuml
    class Host {
        create_game(name: str, words: str) : \n\tcreate a new game. returns game id.
        join_game(game: str) : \n\tclient requests to join a game. returns a bingo board.
        end_game(game: str) : \n\tterminate named game.
        list_games() : \n\treturn all active games.
        play(game: str, move: str) : \n\tadds `move` to `game`.
    }
    class Game {
        plays[]: str

        join() : \n\treturns a bingo card.
        add_play(play: str) : \n\tplayer reports a move.
        get_plays(idx: int) : \n\treturn plays since `idx`.
    }
    class Board {
        buzzwords[]: str
        generate()
    }

    Host "1" *-- "many" Game : games
    Game *-- Board : board
    @enduml

A typical game session would look something like this:

.. uml::
   :caption: Interaction Diagram

    @startuml
    Player -> Host : create_game()
    Host -> Game ** : create
    Game -> Board ** : create
    Host -> Player : game name
    Player -> Host : join_game(game)
    Host -> Game : join()
    Game -> Board : generate()
    Board -> Game : bingo board
    Game -> Host : bingo board
    Host -> Player : bingo board

    loop
    Player -> Host : play(game, move)
    Host -> Game :  add_play(move)
    Player -> Host : get_plays(idx)
    Host -> Game : get_plays(idx)
    Game -> Host : new idx, moves
    Host -> Player : new idx, moves
    end

    Player -> Host : end_game(game)
    Host -> Game !! : destroy
    Game -> Board !! : destroy
    @enduml