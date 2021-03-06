#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

# ---------------------------------
# ---------------------------------


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    query = "DELETE FROM match"
    c.execute(query)
    db.commit()
    db.close()

# ---------------------------------
# ---------------------------------


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    query = "DELETE FROM player"
    c.execute(query)
    db.commit()
    db.close()

# ---------------------------------
# ---------------------------------


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    query = "SELECT COUNT(*) FROM player"
    c.execute(query)
    count = c.fetchone()[0]
    db.close
    return count

# ---------------------------------
# ---------------------------------


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    bleached_name = bleach.clean(name, strip=True)
    c.execute("INSERT INTO player (player_name) values (%s)", (bleached_name,))
    db.commit()
    db.close()

# ---------------------------------
# ---------------------------------


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    c = db.cursor()
    query = "SELECT * FROM standings"
    c.execute(query)
    result = c.fetchall()
    if (result[0][2] != 0) and (result[0][2] == result[1][2]):
        query = "SELECT player_id, player_name, won, played FROM \
        standings ORDER BY (cast(won AS DECIMAL)/played) DESC"
        c.execute(query)
        result = c.fetchall()
    db.close()
    return result

# ---------------------------------
# ---------------------------------


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()
    c.execute("INSERT INTO match (winner, loser) VALUES (%s, %s)",
              (winner, loser,))
    db.commit()
    db.close()

# ---------------------------------
# ---------------------------------


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    result = playerStandings()
    pairings = []
    count = len(result)
    for x in range(0, count - 1, 2):
        paired_list = (result[x][0], result[x][1],
                       result[x + 1][0], result[x + 1][1])
        pairings.append(paired_list)
    return pairings
