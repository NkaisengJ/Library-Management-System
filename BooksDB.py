import sqlite3

class book_database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(" CREATE TABLE IF NOT EXISTS books (title TEXT,author TEXT,isbn TEXT,genre TEXT, availability TEXT)")
        self.conn.commit()

    def add_book(self, title, author, isbn, genre, availability):
        self.cursor.execute("INSERT INTO books VALUES (?, ?, ?, ?, ?)", (title, author, isbn, genre, availability))
        self.conn.commit()

    def delete_book(self, title):
        self.cursor.execute("DELETE FROM books WHERE title = ?", (title,))
        self.conn.commit()

    def update_book(self, title, author, isbn, genre, availability):
        self.cursor.execute("UPDATE books SET title = ?, author = ?, isbn = ?, genre = ?, availability = ? WHERE id = ?", (title, author, isbn, genre, availability))
        self.conn.commit()

    def search_book_by_id(self, isbn):
        self.cursor.execute("SELECT * FROM books WHERE isbn = ?", (isbn,))
        return self.cursor.fetchone()

    def get_all_books(self):
        self.cursor.execute("SELECT * FROM books")
        return self.cursor.fetchall()

    def check_isbn_exists(self, isbn):
        self.cursor.execute("SELECT * FROM books WHERE isbn = ?", (isbn,))
        return self.cursor.fetchone() is not None
    def check_title_exists(self, title):
        self.cursor.execute("SELECT * FROM books WHERE title = ?", (title,))
        return self.cursor.fetchone() is not None