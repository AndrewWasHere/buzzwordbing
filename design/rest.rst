REST Endpoints
==============

Root
----

.. http:get:: /

    Gets a list of active games, with interfaces to delete active games, and
    create a new game.

.. uml::

    @startuml
    salt
    {
      Buzzword Bingo
      Games in Progress:
      * Meeting From Hell | [End]
      * Son of Meeting From Hell | [End]
      ..
      "Game Title" | [New Game]
    }
    @enduml

Game titles are clickable, and take you to the :ref:`Game`. ``New Game`` will
check the game title to make sure it is not in use, create the new game via a
PUT to ``/game_id``, and redirect to the new :ref:`Game`.

``game_id`` is the game title, with spaces removed.

Game
----

.. http:put:: /(str:game_id)

    Create a new game with ``game_id``.

.. http:get:: /(str:game_id)

    Game board. Shows current players, and allows player to join the game.

.. uml::

    @startuml
    salt
    {
      Buzzword Bingo
      Current Players:
      * Alice
      * Bob
      * Charlie
      ..
      "Player Name" | [join]
    }
    @enduml

``Join`` verifies the ``Player Name`` is unique, adds the player to the game,
and redirects to the :ref:`Player` endpoint.

Player
------

.. http:get:: /(str:game_id)/(str:player)

    Creates a new bingo card for player. New GETs of this page will create a
    new bingo card.

.. uml::

    @startuml
    salt
    {
        Buzzword Bingo
        Meeting From Hell
        {#
        lorem | ipsum | dolor | sit | amet
        consectetur | adipiscing | elit | sed | do
        eiusmod | tempor | FREE SPACE | incididunt | ut
        labore | et | dolore | magna | aliqua
        ut | enum | ad | minim | veniam
        }
        {^"Play-by-Play"
        Alice marked 'lorem'.
        Bob marked 'ipsum'.
        Charlie marked 'dolor'.
        Charlie got a BINGO!
        }
    }
    @enduml

When generating this page, the words for the bingo card will be randomized by
the server.

When a player clicks a buzzword on the card, a message will be POSTed to the
:ref:`Player` endpoint indicating that the player selected, or deselected the
buzzword. If the javascript for this page detects a bingo, that information is
POSTed to the :ref:`Player` endpoint in a separate message.

The javascript for this page polls the :ref:`Play By Play` endpoint on a periodic
basis to update its play-by-play window.

.. http:post:: /(str:game_id)/(str:player)

    Report player move.

    :reqjson string event: Player event. Everything after the player name in the play-by-play window. e.g. "marked 'lorem'.", "unmarked 'ipsum'.", "got a BINGO!"

Play By Play
------------

.. http:get:: /(str:game_id)/play-by-play?idx=(int:idx)

    :resjson array events: array of events that happened since ``idx``.
    :resjson float idx: index to send on next query.

If ``idx`` is missing, all events since beginning of game are returned. If
``idx`` is larger than possible index, ``events`` will be empty, and the last
valid ``idx`` is returned.
