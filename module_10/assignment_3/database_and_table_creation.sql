""" 
    Title: pysports_join_queries.py
    Author: Amro Taha
    Date: 07 July 2023
    Description: Database and Table Creation
"""

mysql> CREATE TABLE user (
    user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(75) NOT NULL,
    last_name VARCHAR(75) NOT NULL
);


mysql> CREATE TABLE wishlist (
    wishlist_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user (user_id),
    FOREIGN KEY (book_id) REFERENCES book (book_id)
);


mysql> CREATE TABLE book (
    book_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    book_name VARCHAR(200) NOT NULL,
    details VARCHAR(500),
    author VARCHAR(200) NOT NULL
);


mysql> CREATE TABLE store (
    store_id INT NOT NULL PRIMARY KEY,
    locale VARCHAR(500) NOT NULL
);


mysql> INSERT INTO store (locale) VALUES ('123 Main Street, Anytown, CA 91234');
Query OK, 1 row affected (0.00 sec)
INSERT INTO store (locale) VALUES ('123 Main Street, Anytown, CA 91234');

INSERT INTO book (book_name, details, author) VALUES
('The Hitchhiker''s Guide to the Galaxy', 'A comedy science fiction series created by Douglas Adams.', 'Douglas Adams'),
('Pride and Prejudice', 'A romantic novel of manners written by Jane Austen.', 'Jane Austen'),
('The Lord of the Rings', 'An epic high fantasy trilogy written by J. R. R. Tolkien.', 'J. R. R. Tolkien'),
('Harry Potter and the Sorcerer''s Stone', 'A fantasy novel by J. K. Rowling.', 'J. K. Rowling'),
('The Hunger Games', 'A science fiction novel by Suzanne Collins.', 'Suzanne Collins'),
('The Book Thief', 'A historical novel by Markus Zusak.', 'Markus Zusak'),
('The Fault in Our Stars', 'A young adult novel by John Green.', 'John Green'),
('To Kill a Mockingbird', 'A novel by Harper Lee.', 'Harper Lee');

INSERT INTO user (first_name, last_name) VALUES
('John', 'Doe'),
('Jane', 'Doe'),
('Mary', 'Doe');

INSERT INTO wishlist (user_id, book_id) VALUES
(1, 1),
(1, 2),
(2, 3),
(3, 4);
