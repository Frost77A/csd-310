import mysql.connector

def test_connection():
    try:
        config = {
            "user": "root",
            "password": "snow",
            "host": "127.0.0.1",
            "database": "pysports",
            "port": 3306,
            "raise_on_warnings": True
        }
        connection = mysql.connector.connect(**config)
        print("Connection successful")
    except mysql.connector.Error as e:
        print(e)

if __name__ == "__main__":
    test_connection()
