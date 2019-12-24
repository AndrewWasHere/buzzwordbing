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

    Game *-- Board : board
    @enduml

A typical game session would look something like this:

.. uml::
   :caption: Interaction Diagram

    @startuml
    Player -> Server : PUT /<game_id>
    Server -> Game ** : create
    Game -> Board ** : create
    Server -> Player : <game_id>
    Player -> Server : GET /<game_id>
    Server -> Game : join()
    Game -> Board : generate()
    Board -> Game : bingo board
    Game -> Server : bingo board
    Server -> Player : HTML: game board

    loop
    Player -> Server : POST /<game_id>/<player_id>
    Server -> Game :  add_play(move)
    Player -> Server : GET /<game_id>/play-by-play?idx=<N>
    Server -> Game : get_plays(idx)
    Game -> Server : new idx, moves
    Server -> Player : JSON: new idx, moves
    end

    Player -> Server : DEL /<game_id>
    Server -> Game !! : destroy
    Game -> Board !! : destroy
    @enduml