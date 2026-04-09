import sqlite3

class member_database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS members (
                id INTEGER PRIMARY KEY,
                name TEXT,
                phone TEXT
            )
        """)
        self.conn.commit()

    def add_member(self, id, name, phone):
        self.cursor.execute("INSERT INTO members VALUES (?, ?, ?)", (id, name, phone))
        self.conn.commit()

    def delete_member(self, id):
        self.cursor.execute("DELETE FROM members WHERE id = ?", (id,))
        self.conn.commit()

    def update_member(self, id, name, phone):
        self.cursor.execute("UPDATE members SET name = ?, phone = ? WHERE id = ?", (name, phone, id))
        self.conn.commit()

    def search_member_by_id(self, id):
        self.cursor.execute("SELECT * FROM members WHERE id = ?", (id,))
        return self.cursor.fetchone()

    def get_all_members(self):
        self.cursor.execute("SELECT * FROM members")
        return self.cursor.fetchall()