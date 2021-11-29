import sqlite3

def connect():
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, ing text, tr text)")
	conn.commit()
	conn.close()
	
def insert(ing, tr):
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO book VALUES (NULL, ?, ?)", (ing, tr))
	conn.commit()
	conn.close()

def view():
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM book")
	rows = cur.fetchall()
	conn.close()
	return rows

def search(ing = "", tr = ""):
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM book WHERE ing = ? OR tr = ?", (ing, tr))
	rows = cur.fetchall()
	conn.close()
	return rows

def delete(id):
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("DELETE FROM book WHERE id=?", (id,))
	conn.commit()
	conn.close()

def update(id, ing, tr):
	conn = sqlite3.connect("books.db")
	cur = conn.cursor()
	cur.execute("UPDATE book SET ing = ?, tr = ? WHERE id = ?", (ing, tr, id))
	conn.commit()
	conn.close()

connect()

