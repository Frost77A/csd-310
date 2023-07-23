""" 
    Title: whatabook.py
    Author: Amro Taha
    Date: 22 July 2023
    Description: WhatABook program; Console program that interfaces with a MySQL database
"""
import mysql.connector

# Establishing a database connection
cnx = mysql.connector.connect(user='root', password='snow', host='localhost', database='whatabook')
cursor = cnx.cursor()

# Method to display the main menu
def show_menu():
    print("Menu:")
    print("1. View Books")
    print("2. View Store Locations")
    print("3. My Account")
    print("4. Exit Program")

# Method to display the list of books
def show_books(cursor):
    cursor.execute("SELECT book_id, book_name, author, details FROM book")
    books = cursor.fetchall()
    
    print("Books:")
    for book in books:
        print("Book ID:", book[0])
        print("Book Name:", book[1])
        print("Author:", book[2])
        print("Details:", book[3])
        print("")

# Method to display the store locations
def show_locations(cursor):
    cursor.execute("SELECT location_id, location_name, address FROM location")
    locations = cursor.fetchall()
    
    print("Store Locations:")
    for location in locations:
        print("Location ID:", location[0])
        print("Location Name:", location[1])
        print("Address:", location[2])
        print("")

# Method to validate the user
def validate_user():
    user_id = input("Enter your user ID: ")
    # Perform validation logic here
    return user_id

# Method to display the account menu
def show_account_menu():
    print("Account Menu:")
    print("1. Wishlist")
    print("2. Add Book")
    print("3. Main Menu")
    print("4. Exit Program")

# Method to display the user's wishlist
def show_wishlist(cursor, user_id):
    query = "SELECT b.book_id, b.book_name, b.author, b.details FROM book b INNER JOIN wishlist w ON b.book_id = w.book_id WHERE w.user_id = %s"
    cursor.execute(query, (user_id,))
    wishlist = cursor.fetchall()
    
    print("Wishlist:")
    for book in wishlist:
        print("Book ID:", book[0])
        print("Book Name:", book[1])
        print("Author:", book[2])
        print("Details:", book[3])
        print("")

# Method to display the available books to add to the wishlist
def show_books_to_add(cursor, user_id):
    query = "SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = %s)"
    cursor.execute(query, (user_id,))
    available_books = cursor.fetchall()
    
    print("Available Books:")
    for book in available_books:
        print("Book ID:", book[0])
        print("Book Name:", book[1])
        print("Author:", book[2])
        print("Details:", book[3])
        print("")

# Method to add a book to the user's wishlist
def add_book_to_wishlist(cursor, user_id, book_id):
    query = "INSERT INTO wishlist (user_id, book_id) VALUES (%s, %s)"
    cursor.execute(query, (user_id, book_id))
    cnx.commit()
    print("Book added to wishlist.")

# Custom input function to validate numeric choices
def get_numeric_choice(prompt, valid_choices):
    while True:
        choice = input(prompt)
        if choice in valid_choices:
            return choice
        print("Invalid input. Please enter a valid numeric choice.")

# Main program loop
while True:
    show_menu()
    choice = get_numeric_choice("Enter your choice: ", ["1", "2", "3", "4"])

    if choice == "1":
        show_books(cursor)
    elif choice == "2":
        show_locations(cursor)
    elif choice == "3":
        user_id = validate_user()
        if user_id:
            while True:
                show_account_menu()
                account_choice = get_numeric_choice("Enter your choice: ", ["1", "2", "3", "4"])

                if account_choice == "1":
                    show_wishlist(cursor, user_id)
                elif account_choice == "2":
                    show_books_to_add(cursor, user_id)
                    book_id = input("Enter the book ID to add to your wishlist: ")
                    add_book_to_wishlist(cursor, user_id, book_id)
                elif account_choice == "3":
                    break
                elif account_choice == "4":
                    exit()
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid user ID. Please try again.")
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")

# Closing the database connection
cursor.close()
cnx.close()
