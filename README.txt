* -------------------------- *
TOURNAMENT WITH SWISS PAIRINGS
* -------------------------- *
by Philipp Bechhaus
Udacity Back-End Developer, part of IPND



* -------------------------- *
INTRODUCTION
* -------------------------- *

The underlying program is based on Python code that makes use of a PostreSQL database that
is initiated and filled through prewritten SQL code.



* -------------------------- *
EXECUTION
* -------------------------- *

##############################
preparation
##############################
In order to get started, one must make sure that:
- Virtual Machine &
- VAGRANT
are properly installed on ones computer.

##############################
written overview
##############################
Once that has been done, one must follow the steps:
- open TERMINAL (or similar console) and execute CHANGE DIR command to access tournament program folder
- power up the VAGRANT machine
- log into the VAGRANT machine
- change directory inside the initiated Virtual Machine
- initiate SQL database via PostgreSQL commands
- execute PYTHON file

##############################
code overview
##############################
1.  LAUNCH TERMINAL
2.  $ cd /users/((name))/fullstack/vagrant
3.  $ vagrant up
4.  $ vagrant ssh
5.  $ cd /vagrant/tournament
6.  $ psql
7.  => \i tournament.sql
8.  => \q
9.  $ python tournament_test.py

##############################
tournament_test.py result
##############################
If everything has been set up properly the prompt should show:
1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
Success!  All tests pass!

* -------------------------- *
THANK YOU
* -------------------------- *
