""" 
    Title: pysports_join_queries.py
    Author: Amro Taha
    Date: 07 July 2023
    Description: Test program for joining the player and team tables
"""
import mysql.connector
from connection_config import connection_config
from mysql.connector import errorcode

try:
    # Connect to the MySQL database
    db = mysql.connector.connect(**connection_config)

    # Output the connection status
    print("\n  Database user {} connected to MySQL on host {} with database {}".format(connection_config["user"], connection_config["host"], connection_config["database"]))

    input("\n\n  Press any key to continue...")

    # Rest of your code...

    # Define a function to execute an inner join on the player and team tables
    def show_players(cursor, title):
        """
        Method to execute an inner join on the player and team table,
            iterate over the dataset and output the results to the terminal window.
        """

        # Inner join query
        cursor.execute("""
            SELECT player_id, first_name, last_name, team_name
            FROM player
            INNER JOIN team ON player.team_id = team.team_id
        """)

        # Get the results from the cursor object
        players = cursor.fetchall()

        # Print the title
        print("\n  -- {} --".format(title))

        # Iterate over the player data set and display the results
        for player in players:
            print(
                "  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}".format(
                    player[0], player[1], player[2], player[3]
                )
            )

    # Create a cursor object
    cursor = db.cursor()

    # Call the show_players function
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

except mysql.connector.Error as err:
    # Handle MySQL database errors
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password is invalid")
    elif err.errno == errorcodes.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
    else:
        print(err)

finally:
    # Close the connection to MySQL
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()
        print("\n  Database connection closed.")
