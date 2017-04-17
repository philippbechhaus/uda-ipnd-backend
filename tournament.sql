-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--
-- INTRO NOTES END
--

-- Delete previous DATABASE (if existing)
DROP DATABASE IF EXISTS tournament;
-- *----------------------


-- Initiate new DATABASE
CREATE DATABASE tournament;
-- *----------------------


-- Connect to new DATABASE
\connect tournament;
-- *----------------------


-- Initiate TABLE <player>
CREATE TABLE player(
  player_id serial PRIMARY KEY,
  player_name text
);
-- *----------------------


-- Initiate TABLE <match>
CREATE TABLE match (
  match_id serial PRIMARY KEY,
  winner INTEGER,
  loser INTEGER,
  FOREIGN KEY(winner) REFERENCES player(player_id),
  FOREIGN KEY(loser) REFERENCES player(player_id)
);
-- *----------------------


-- Create VIEW as dashboard to see standings
CREATE VIEW standings AS
SELECT p.player_id as player_id, p.player_name,
(SELECT count(*) FROM match WHERE match.winner = p.player_id) as won,
(SELECT count(*) FROM match WHERE p.player_id in (winner, loser)) as played
FROM player p
GROUP BY p.player_id
ORDER BY won DESC;
-- *----------------------

-- END
