""" 
    Title: pysports_queries.py
    Author: Amro Taha
    Date: 07/02/2023
    Description: Test program for executing queries against the pysports database. 
"""

import mysql.connector
from mysql.connector import errorcodes

def main():
    """ Connect to the pysports database """
    config = {
        "user": "root",
        "password": "snow",
        "host": "127.0.0.1",
        "database": "pysports",
        "port": "3306",
        "raise_on_warnings": True
    }
    db = mysql.connector.connect(**config)

    """ Create a cursor object """
    cursor = db.cursor()

    """ Execute a query to select all teams """
    cursor.execute("SELECT team_id, team_name, mascot FROM team")

    """ Fetch all the rows from the result set """
    teams = cursor.fetchall()

    """ Print the results """
    print("\n  -- DISPLAYING TEAM RECORDS --")
    for team in teams:
        print("  Team ID: {}\n  Team Name: {}\n  Mascot: {}\n".format(team[0], team[1], team[2]))

    """ Execute a query to select all players """
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    """ Fetch all the rows from the result set """
    players = cursor.fetchall()

    """ Print the results """
    print ("\n  -- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

    """ Close the cursor object """
    cursor.close()

    """ Close the connection to the database """
    db.close()

if __name__ == "__main__":
    main()
