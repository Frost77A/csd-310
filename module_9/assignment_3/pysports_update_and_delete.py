"""
Title: pysports_update_and_delete.py
Author: Amro Taha
Date: 07 July 2023
Description: Test program for inserting, updating, and deleting records from the pysports database
"""

import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    "user": "root",
    "password": "snow",
    "host": "127.0.0.1",
    "database": "pysports",
    "port": "3306",
    "raise_on_warnings": True
}

def connect_to_database():
    try:
        # Connect to the database
        db = mysql.connector.connect(**config)
        print("Connection successful")
        return db
    except mysql.connector.Error as err:
        # Handle connection errors
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("The supplied username or password is invalid")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("The specified database does not exist")
        else:
            print(err)
        return None

def insert_player(cursor, first_name, last_name, team_id):
    # Insert a new player record
    insert_query = "INSERT INTO player (first_name, last_name, team_id) VALUES (%s, %s, %s)"
    player_data = (first_name, last_name, team_id)
    cursor.execute(insert_query, player_data)

def update_player(cursor, player_id, team_id):
    # Update the player's team
    update_query = "UPDATE player SET team_id = %s WHERE player_id = %s"
    update_values = (team_id, player_id)
    cursor.execute(update_query, update_values)

def delete_player(cursor, player_id):
    # Delete the player record
    delete_query = "DELETE FROM player WHERE player_id = %s"
    delete_value = (player_id,)
    cursor.execute(delete_query, delete_value)

def show_players(cursor, title):
    # Inner join query to display player records with team names
    query = """
    SELECT player.player_id, player.first_name, player.last_name, team.team_name
    FROM player
    INNER JOIN team ON player.team_id = team.team_id
    """
    cursor.execute(query)
    players = cursor.fetchall()

    print("\n  -- {} --".format(title))
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}".format(
            player[0], player[1], player[2], player[3]
        ))

def validate_integer_input(value):
    if not value.isdigit():
        raise ValueError("Invalid input. Expected an integer.")
    return int(value)

def validate_name_input(value, field_name):
    if not value.replace(" ", "").isalpha():
        raise ValueError("Invalid {} input. Expected alphabetic characters only.".format(field_name))
    return value

def validate_player_existence(cursor, player_id):
    # Check if the player exists in the database
    query = "SELECT COUNT(*) FROM player WHERE player_id = %s"
    cursor.execute(query, (player_id,))
    result = cursor.fetchone()
    return result[0] > 0

def validate_team_existence(cursor, team_id):
    # Check if the team exists in the database
    query = "SELECT COUNT(*) FROM team WHERE team_id = %s"
    cursor.execute(query, (team_id,))
    result = cursor.fetchone()
    return result[0] > 0

if __name__ == "__main__":
    # Connect to the MySQL database
    db = connect_to_database()
    if db is None:
        exit()

    # Create a cursor object
    cursor = db.cursor()

    # Insert a new player record
    first_name = input("Enter the player's first name: ")
    last_name = input("Enter the player's last name: ")
    team_id = input("Enter the team ID: ")

    # Validate inputs
    try:
        first_name = validate_name_input(first_name, "First Name")
        last_name = validate_name_input(last_name, "Last Name")
        team_id = validate_integer_input(team_id)
    except ValueError as e:
        print(str(e))
        exit()

    insert_player(cursor, first_name, last_name, team_id)

    # Display player records after insertion
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    # Get the player ID to update
    player_id = input("Enter the player ID to update: ")

    # Validate inputs
    try:
        player_id = validate_integer_input(player_id)
        if not validate_player_existence(cursor, player_id):
            raise ValueError("Invalid player ID. Player does not exist.")
    except ValueError as e:
        print(str(e))
        exit()

    #
