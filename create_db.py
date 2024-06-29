import sqlite3

conn = sqlite3.connect("database.db")
print("Connected to database successfully")

conn.execute('CREATE TABLE faces(name TEXT NOT NULL, encoding TEXT NOT NULL)');
print("Table Created Successfully")

conn.close()